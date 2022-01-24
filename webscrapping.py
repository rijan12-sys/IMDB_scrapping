
from pip._vendor import requests
from bs4 import BeautifulSoup

number_of_movies = input("Please enter the number of movies you want to search? ")

url = "https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&count=" + number_of_movies
# print(url)
url_response = requests.get(url)
# print(url_response.content)
parseHTML = BeautifulSoup(url_response.content, "html.parser")

for movies in parseHTML.findAll('div', class_="lister-item mode-advanced"):
    print(movies.h3.a.text)
    print("genre: " + (movies.find("span", class_="genre").text.strip()))
    print("ratings: " + movies.strong.text)
    link_of_movies = movies.h3.a.get("href")
    print("https://www.imdb.com/" +link_of_movies)
    print("************************************")
    

    

    
