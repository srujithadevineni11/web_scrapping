#webscrapping a livewebsite where there will be latest tech news 
#we will be scrapping the titles and link of each news article published there 
#the website we are going to use here is 
#https://news.ycombinator.com/
#finally based on rating we will get the highest news article name and link  

#to get the html of the page 
from bs4 import BeautifulSoup
import requests
url="https://news.ycombinator.com/"
response=requests.get(url)
#response
#response.text
soup=BeautifulSoup(response.text,"html.parser")
#soup

#to store data as a list
text_list=[]
link_list=[]
score_list=[]

#getting each text and link and adding it into the list 
tags=soup.find_all(name='span',class_='titleline')
for i in tags:
    text=i.get_text()
    text_list.append(text)
    link=i.a.get("href")
    link_list.append(link)
    
#'111 points' we will get like this when we scrape
#normally we have to change them into just integer score 
#so to do that we use the split method two split the
#the string and then index method to get the first string 
#and we change everything into int to get the list numbers as integers 

score=soup.find_all(name='span',class_='score')
for j in score:
    score_text=int(j.get_text().split()[0])
    score_list.append(score_text)
    
#to see if we got the data correct or not 
#print(text_list)
#print(link_list)
#print(score_list)

high=max(score_list)
high
high_index=score_list.index(high)
#high_index
text_list[high_index]
link_list[high_index]

print("\nThis is the current highest news article : "+text_list[high_index])
print("\nlink to that article : "+link_list[high_index])
