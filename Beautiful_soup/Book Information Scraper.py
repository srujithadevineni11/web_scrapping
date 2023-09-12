#webscrapping a bookswebsite and getting its 
#produxt name
#product price
#product rating
#the website used here is https://books.toscrape.com'
#and making a table which has the book name and corresponding price and ratings .

#to get the html of the page
import requests
from bs4 import BeautifulSoup
url = 'https://books.toscrape.com'
response=requests.get(url) 
soup=BeautifulSoup(response.text,'html.parser')

#to store data as a list
book_list=[]
price_list=[]
rating_list=[]

#getting each book name and adding it into the book list 
for i in soup.find_all(name='h3'):
    book_list.append(i.a['title'])
    
book_list 

#getting each book price and adding it into the book price list 
for j in soup.find_all('p',class_='price_color'):
    price_list.append(j.get_text())

price_list

#getting each book rating and adding it into the book rating list 
for k in soup.find_all(name='article',class_='product_pod'):
   rating_list.append(k.p['class'][1])

rating_list

    
import pandas as pd #to accsess data frames we use this

table=pd.DataFrame({'Book Name':book_list ,'Price':price_list ,'Ratings':rating_list})


               

