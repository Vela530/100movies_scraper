from bs4 import BeautifulSoup
import requests



response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

movies = response.text


soup = BeautifulSoup(movies, "html.parser")


movie_list = [i.get_text() for i in soup.find_all(name="h3", class_="title")]

movie_list.reverse()

with open("100movies\movie_watch.txt", "w", encoding='utf-8') as file:
    for movie in movie_list:
        file.write(f"{movie}\n")
    file.close()


print(movie_list)