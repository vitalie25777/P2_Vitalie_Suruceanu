

import requests
from bs4 import BeautifulSoup
import pandas as pd

books = []
# for i in range(3):

url = 'http://books.toscrape.com/index.html'
host = "http://books.toscrape.com"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
content = soup.find_all("article", class_="product_pod")

for product_pod in content:
    books.append({

        "titres": product_pod.find("h3").text,
        "prix": product_pod.find("p", class_="price_color").text,
        "links": host + product_pod.find("a").get("href"),
        "images": host + product_pod.find("img", class_="thumbnail").get("src"),

    })

print(books)

df = pd.DataFrame(books)
df.to_csv("books_1.csv")
df.to_excel("books.xlsx")
print("saved to file")
