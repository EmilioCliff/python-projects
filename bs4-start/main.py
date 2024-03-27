from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
website_code = BeautifulSoup(response.text, "html.parser")
article_tag = website_code.find_all(name="span", class_="titleline")
upvotes = []
article_url = []
article_title = []
for tag in article_tag:
    article_url.append(tag.find("a").get("href"))
    article_title.append(tag.find("a").string)

article_upvotes = website_code.find_all(name="span", class_="score")
for upvote in article_upvotes:
    upvotes.append(int(upvote.getText().split()[0]))

largest_upvote = max(upvotes)
index_largest_upvote = upvotes.index(largest_upvote)
print(article_title[index_largest_upvote + 1])
print(article_url[index_largest_upvote + 1])
print(upvotes[index_largest_upvote])
# with open("./website.html", "r") as data:
#     website_data = data.read()
#
# soup = BeautifulSoup(website_data, "html.parser")
# print(soup.find("h3")['heading'])
