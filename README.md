# web_scrapping projects

This repository contains various web scraping projects using BeautifulSoup and Selenium.

## BeautifulSoup Projects

### project-1:Tech News Scraper https://github.com/srujithadevineni11/web_scrapping/blob/main/Beautiful_soup/project1.py 

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


### project-2: Top 100 Movies List https://github.com/srujithadevineni11/web_scrapping/blob/main/Beautiful_soup/project2.py 
output file https://github.com/srujithadevineni11/web_scrapping/blob/main/Beautiful_soup/project2_movies.txt 

This project scrapes the list of the top 100 movies to watch from [Empire Online](https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/). It extracts the movie titles and saves them to a text file for easy reference.

### How it Works

1. The script sends a GET request to the website to fetch the HTML content of the page.

2. It uses BeautifulSoup to parse the HTML and extract the movie titles displayed on the page.

3. The script stores the movie titles in a text file named "movies.txt," starting from the 1st top-rated movie to the 100th top-rated movie.

### Prerequisites

Before running the script, make sure you have the following Python libraries installed:

- BeautifulSoup4
- requests

You can install them using pip:

pip install beautifulsoup4 requests

### project-3 Book Information Scraper https://github.com/srujithadevineni11/web_scrapping/blob/main/Beautiful_soup/project4.py

This project scrapes book information from [books.toscrape.com](https://books.toscrape.com) and creates a table containing the book name, price, and ratings.

### How it Works

1. The script sends a GET request to the website to fetch the HTML content of the page.

2. It uses BeautifulSoup to parse the HTML and extract information about the books, including their names, prices, and ratings.

3. The script organizes this data into a table using the Pandas library.

4. The resulting table contains columns for Book Name, Price, and Ratings.

### Prerequisites

Before running the script, make sure you have the following Python libraries installed:

- BeautifulSoup4
- requests
- Pandas

### You can install them using pip:

pip install beautifulsoup4 requests pandas

### Project4: Stock Information Scraper https://github.com/srujithadevineni11/web_scrapping/blob/main/Beautiful_soup/project5.py 

This project scrapes stock information from [MarketWatch](https://www.marketwatch.com/investing/stock/aapl?mod=search_symbol) for a specific stock (in this case, Apple - AAPL). It extracts the stock's current price, closing price, 52-week range (lower and upper), and analyst rating.

### How it Works

1. The script sends a GET request to the MarketWatch website to fetch the HTML content of the page.

2. It uses BeautifulSoup to parse the HTML and extract information about the stock, including its current price, closing price, 52-week range, and analyst rating.

3. The script then prints out the extracted information.

### Prerequisites

Before running the script, make sure you have the following Python libraries installed:

- BeautifulSoup4
- requests

### You can install them using pip:

pip install beautifulsoup4 requests

