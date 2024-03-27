import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
soup = BeautifulSoup(response.text, "html.parser")
movie_tags = soup.find_all("h3", class_="title")
movie_names = [movie_tag.getText() for movie_tag in movie_tags][::-1]
with open("movies_to_watch.txt", "w") as file:
    for movie_name in movie_names:
        file.write(f"{movie_name}\n")
