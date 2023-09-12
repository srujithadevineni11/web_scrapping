# web_scrapping projects
This repository contains various web scraping projects using BeautifulSoup and Selenium.

## BeautifulSoup Projects.

### -Flipkart Price Tracker https://github.com/srujithadevineni11/web_scrapping/blob/main/Beautiful_soup/flipkart_webscrapping.py 

This Python script tracks the price of a product on Flipkart and sends an email notification when the price falls below a certain threshold. It allows you to stay updated on price changes and make informed purchase decisions.

#### Features

- Monitors the price of a specific product on Flipkart.
- Sends an email notification when the price drops below a user-defined threshold.
- Configurable through a simple configuration section at the top of the script.

#### Prerequisites

Before using this script, ensure that you have the following:

- Python 3.x installed on your machine.
- The required Python packages (`requests`, `smtplib`, `bs4`) installed. You can install them using `pip`:
  pip install requests smtplib bs4

#### Configuration

Before running the script, update the following variables in the script with your information:

URL: The URL of the Flipkart product you want to track.
EMAIL: Your Gmail email address (used for sending notifications).
PASSWORD: Your Gmail app password (generate one from your Google Account settings).
RECEIVER_EMAIL: The email address where you want to receive price drop notifications.
PRICE_THRESHOLD: The desired price threshold. When the product price falls below this value, you will be notified.


### -Tech News Scraper https://github.com/srujithadevineni11/web_scrapping/blob/main/Beautiful_soup/Tech%20News%20Scraper.py 

This project scrapes the latest technology news articles from [news.ycombinator.com](https://news.ycombinator.com/) and finds the highest-rated article based on user ratings.

#### How it Works.

1. The script sends a GET request to the website [news.ycombinator.com](https://news.ycombinator.com/) to fetch the HTML content of the page.

2. It uses BeautifulSoup to parse the HTML and extract information about the news articles, including their titles and links.

3. The script also extracts the user rating scores of each news article. These scores are typically in the format "111 points," and the script converts them into integers.

4. After collecting the data, the script identifies the news article with the highest rating and provides the title and link to that article.

#### Prerequisites

Before running the script, make sure you have the following Python libraries installed:

- BeautifulSoup4
- requests

#### You can install them using pip:

pip install beautifulsoup4 requests.


### -Top 100 Movies List https://github.com/srujithadevineni11/web_scrapping/blob/main/Beautiful_soup/project2.py 
output file https://github.com/srujithadevineni11/web_scrapping/blob/main/Beautiful_soup/project2_movies.txt 

This project scrapes the list of the top 100 movies to watch from [Empire Online](https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/). It extracts the movie titles and saves them to a text file for easy reference.

#### How it Works

1. The script sends a GET request to the website to fetch the HTML content of the page.

2. It uses BeautifulSoup to parse the HTML and extract the movie titles displayed on the page.

3. The script stores the movie titles in a text file named "movies.txt," starting from the 1st top-rated movie to the 100th top-rated movie.

#### Prerequisites

Before running the script, make sure you have the following Python libraries installed:

- BeautifulSoup4
- requests

You can install them using pip:

pip install beautifulsoup4 requests

### -Book Information Scraper https://github.com/srujithadevineni11/web_scrapping/blob/main/Beautiful_soup/Book%20Information%20Scraper.py 
This project scrapes book information from [books.toscrape.com](https://books.toscrape.com) and creates a table containing the book name, price, and ratings.

#### How it Works

1. The script sends a GET request to the website to fetch the HTML content of the page.

2. It uses BeautifulSoup to parse the HTML and extract information about the books, including their names, prices, and ratings.

3. The script organizes this data into a table using the Pandas library.

4. The resulting table contains columns for Book Name, Price, and Ratings.

#### Prerequisites

Before running the script, make sure you have the following Python libraries installed:

- BeautifulSoup4
- requests
- Pandas

#### You can install them using pip:

pip install beautifulsoup4 requests pandas

### -Stock Information Scraper https://github.com/srujithadevineni11/web_scrapping/blob/main/Beautiful_soup/Stock%20Information%20Scraper.py

This project scrapes stock information from [MarketWatch](https://www.marketwatch.com/investing/stock/aapl?mod=search_symbol) for a specific stock (in this case, Apple - AAPL). It extracts the stock's current price, closing price, 52-week range (lower and upper), and analyst rating.

#### How it Works

1. The script sends a GET request to the MarketWatch website to fetch the HTML content of the page.

2. It uses BeautifulSoup to parse the HTML and extract information about the stock, including its current price, closing price, 52-week range, and analyst rating.

3. The script then prints out the extracted information.

#### Prerequisites

Before running the script, make sure you have the following Python libraries installed:

- BeautifulSoup4
- requests

#### You can install them using pip:

pip install beautifulsoup4 requests


# Selenium projects 

## -LinkedIn Data Scraper https://github.com/srujithadevineni11/web_scrapping/blob/main/selenium/linkedin_project_selenium_final.py 

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

## -PDF Downloader for FID4SA Repository https://github.com/srujithadevineni11/web_scrapping/blob/main/selenium/npl_pdfs_download_project_final.py

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

