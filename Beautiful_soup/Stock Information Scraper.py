#webscrapping a stocks website to get
#the price of the stock
#closing price of the stock
#52 week range(lower,upper)
#analayst rating 
#the website we are going to use marketwatch in that we are scraping apple stocks 
#the link to it is https://www.marketwatch.com/investing/stock/aapl?mod=search_symbol

#to get the html of the page
import requests
from bs4 import BeautifulSoup
url='https://www.marketwatch.com/investing/stock/aapl?mod=search_symbol'
page=requests.get(url)
page
soup=BeautifulSoup(page.text,"lxml")
soup

#To get price of the stock
price=soup.find('bg-quote',{'class':'value'}).text

#To get closing price of the stock
closing_price=soup.find('td',{'class':'table__cell u-semi'})

#To get 52 week range(lower,upper)
week=soup.find('mw-rangebar',{'class':'element element--range range--yearly'})
lower=week.find_all('span',{'class':'primary'})[0].text
upper=week.find_all('span',{'class':'primary'})[1].text

#analayst rating 
rating=soup.find('li',{'class':'analyst__option active'}).text

print("The price of the stock : "+price)
print("Closing price of the stock : "+closing_price.text)
print("52 week range lower is : "+lower+"\n"+"52 week range upper is : "+upper)
print("Analayst rating : "+rating)
