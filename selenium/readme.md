# Selenium projects 

## LinkedIn Data Scraper

### Description

This Python script is designed for web scraping purposes, specifically for extracting data from LinkedIn profiles. It uses the Selenium library to automate the process of logging into LinkedIn and collecting information from a list of LinkedIn profile links provided in an Excel file. The script extracts and stores data such as names, college names, locations, and work experience from the LinkedIn profiles.

### Usage

Installation: Make sure you have Python installed on your system.
Install the necessary libraries using pip: pip install selenium pandas openpyxl
Download the appropriate Chrome WebDriver for your system and update the webdriver.Chrome() line with the correct path to the WebDriver.
Running the Script:Modify the linkedin_username and linkedin_password variables with your LinkedIn login credentials.
Provide an Excel file with a column named "Linkedin Link" containing the LinkedIn profile URLs you want to scrape.
Run the script:python linkedin_scraper.py

The script will scrape data from the LinkedIn profiles and store it in a new Excel file.
Output: The scraped data will be saved in an Excel file named "108_students_data.xlsx."

### Dependencies

Selenium
Pandas
openpyxl (for Excel handling)
Example

## Disclaimer

This script is intended for educational and research purposes only. Make sure you comply with LinkedIn's terms of service and privacy policy when using it. Be respectful and responsible when scraping data from websites.


