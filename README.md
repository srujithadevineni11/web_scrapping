# web_scrapping projects

This repository contains various web scraping projects using BeautifulSoup and Selenium.

# BeautifulSoup Projects
project-1:https://github.com/srujithadevineni11/web_scrapping/blob/main/Beautiful_soup/project1.py  Tech News Scraper

This project scrapes the latest technology news articles from [news.ycombinator.com](https://news.ycombinator.com/) and finds the highest-rated article based on user ratings.

How it Works

1. The script sends a GET request to the website [news.ycombinator.com](https://news.ycombinator.com/) to fetch the HTML content of the page.

2. It uses BeautifulSoup to parse the HTML and extract information about the news articles, including their titles and links.

3. The script also extracts the user rating scores of each news article. These scores are typically in the format "111 points," and the script converts them into integers.

4. After collecting the data, the script identifies the news article with the highest rating and provides the title and link to that article.

Prerequisites

Before running the script, make sure you have the following Python libraries installed:

- BeautifulSoup4
- requests

You can install them using pip:
```bash
pip install beautifulsoup4 requests.


project-2:
