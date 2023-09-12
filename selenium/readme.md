# Selenium projects 

## -LinkedIn Data Scraper

#### Description

This Python script is designed for web scraping purposes, specifically for extracting data from LinkedIn profiles. It uses the Selenium library to automate the process of logging into LinkedIn and collecting information from a list of LinkedIn profile links provided in an Excel file. The script extracts and stores data such as names, college names, locations, and work experience from the LinkedIn profiles.

#### Usage

Installation: Make sure you have Python installed on your system.

Install the necessary libraries using pip: pip install selenium pandas openpyxl

Download the appropriate Chrome WebDriver for your system and update the webdriver.Chrome() line with the correct path to the WebDriver.

Running the Script:Modify the linkedin_username and linkedin_password variables with your LinkedIn login credentials.

Provide an Excel file with a column named "Linkedin Link" containing the LinkedIn profile URLs you want to scrape.

Run the script:python linkedin_scraper.py

The script will scrape data from the LinkedIn profiles and store it in a new Excel file.

Output: The scraped data will be saved in an Excel file named "108_students_data.xlsx."

#### Dependencies

Selenium

Pandas

openpyxl (for Excel handling)

Example

#### Disclaimer

This script is intended for educational and research purposes only. Make sure you comply with LinkedIn's terms of service and privacy policy when using it. Be respectful and responsible when scraping data from websites.

## -PDF Downloader for FID4SA Repository

#### Description

This Python script automates the process of downloading PDF files from the FID4SA Repository website. It uses Selenium, BeautifulSoup, and the Chrome WebDriver to navigate the website, locate PDF download links, and download the PDF files to a specified folder.

#### Usage

Installation:Make sure you have Python installed on your system.

Install the necessary libraries using pip:pip install selenium beautifulsoup4

Download the appropriate Chrome WebDriver for your system and specify the path to the WebDriver in the chromedriver_path variable.

Configuration:Specify the folder where you want to download the PDFs by setting the download_folder variable.

Customize the Chrome options in chrome_options as needed, such as setting preferences for downloading PDFs.

Running the Script:Modify the url variable to point to the web page containing the PDF links you want to download.

Run the script:python pdf_downloader.py

The script will navigate the website, find and download PDF files to the specified folder.

#### Dependencies

Selenium

BeautifulSoup4
