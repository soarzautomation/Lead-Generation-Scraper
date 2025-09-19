# Lead-Generation-Scraper
This project is a powerful Python tool designed to automate the process of gathering business leads from public online directories. It transforms the slow, manual task of copying and pasting contact information into a fast, reliable, and automated workflow.

## The Business Problem
Sales teams, marketing agencies, and small business owners often spend countless hours manually searching websites like Yellow Pages or other directories to build lead lists. This process is not only time-consuming but also prone to human error, resulting in incomplete or inaccurate data.

## The Solution and Business Impact
This automation script provides a robust solution to this problem, delivering significant and measurable benefits:
- **Massive Time Savings**: Turns a multi-day manual research task into a process that can be completed in minutes or hours.
- **Data Accuracy**: Eliminates typos and copy-paste errors, ensuring the lead list is clean and reliable.
- **Structured, Usable Data**: Provides the output in a clean, ready-to-use CSV format that can be directly imported into a CRM or used for marketing campaigns.
- **Strategic Focus**: Frees up your team to focus on what they do best--reaching out to potential clients and closing sales--instead of getting bogged down in manual data collection.

## How It Works
This tool is build with a clean, modular Python script. It uses the **Requests** library to download web pages and **BeautifulSoup** to intelligently parse the HTML. It is designed to handle navigating through multiple pages of search results and gracefully manage entries where some information (like a website) might be missing.

## How to Use
This tool is designed to be run from the command line. Follow these steps to generate your own lead list:
### 1. Prerequisites
- Ensure you have Python 3.8+ installed on your system.
- It is highly recommended to use a virtual environment to manage dependencies.

### 2. Installation
Clone this repository to your local machine and install the required packages:
```bash
# Clone the repository
git clone https://github.com/soarzautomation/Lead-Generation-Scraper.git

# Navigate into the project directory
cd Lead-Generation-Scraper

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate # On Windows, use `ven\Scripts\activate`

# Install the require packages
pip install -r requirements.txt
```

### 3. Execution
The script is configured to run with a specific target URL. To start the scraping process, simply run the script from your terminal:
```bash
python scraper.py
```
The script will then begin scraping the data and save the final output as a `.csv` file in the project directory.
