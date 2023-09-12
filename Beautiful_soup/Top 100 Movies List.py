#webscrapping a moviewebsite , here in this website
# we have a list of 100 top movies to watch so we going to 
#scrape just the movie titles from top rated to least ,
#to make our work easy of searching for movies every time in that website 
#the link fot the website we are going to scrape
#https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/

#to get the html of the page 
import requests
from bs4 import BeautifulSoup
url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'
response=requests.get(url) 
soup=BeautifulSoup(response.text,'html.parser')

#to store data as a list
movie_list=[]
#getting each moving name and adding it into the list 
movie=soup.find_all('h3',class_='title')
for i in movie:
    movie_name=i.get_text()
    movie_list.append(movie_name)
    
#copying the movies names in reverse order as the website displays the 
#movies from 100th top movie to 1 st top movie here we are saving it from 
#1st top movie to 100th top movie in our file .
with open("movies.txt",mode='w') as file:
    for j in range(len(movie_list)-1,-1,-1):
        file.write(f"{movie_list[j]}\n")
        
