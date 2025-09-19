import requests
import sys
from bs4 import BeautifulSoup
import csv
import time

def fetch_page(url):
    """
    Fetches the raw content (bytes) of a web page.
    """
    print(f"Fetching: {url}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching the page: {e}")
        return None

def parse_content(html_bytes):
    """
    Parses the HTML to extract book titles and prices, and finds the next page link.
    """
    soup = BeautifulSoup(html_bytes, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    
    scraped_data = []
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        scraped_data.append({'title': title, 'price': price})
    
    # --- Find the link to the next page ---
    next_page_element = soup.find('li', class_='next')
    if next_page_element and next_page_element.a:
        next_page_url = next_page_element.a['href']
        return scraped_data, next_page_url
    else:
        return scraped_data, None

def save_to_csv(data, filename):
    """
    Saves the scraped data to a CSV file.
    """
    print(f"\n💾 Saving all data to '{filename}'...")
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'price']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print("✅ Data successfully saved.")
    except IOError as e:
        print(f"❌ Error saving file: {e}")
        sys.exit(1)

def scrape_all_pages(base_url):
    """
    Manages the scraping of all pages.
    """
    all_books_data = []
    current_url = base_url
    
    while current_url:
        html_content = fetch_page(current_url)
        if html_content:
            data, next_page_suffix = parse_content(html_content)
            all_books_data.extend(data)
            
            if next_page_suffix:
                # Construct the full URL for the next page
                current_url = base_url.rsplit('/', 1)[0] + '/' + next_page_suffix
            else:
                # No more pages to scrape
                current_url = None
                print("\nReached the last page.")
        else:
            # Stop if a page fails to download
            current_url = None
            
        time.sleep(1) # Be a good internet citizen and pause between requests
        
    return all_books_data

# --- Main execution block ---
if __name__ == "__main__":
    # The starting URL for the first page
    start_url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'
    output_filename = 'all_scraped_books.csv'
    
    all_data = scrape_all_pages(start_url)
    
    if all_data:
        print(f"\n✅ Total books scraped: {len(all_data)}")
        save_to_csv(all_data, output_filename)