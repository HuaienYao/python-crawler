from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
print(html)

soup = BeautifulSoup(html, features='lxml')
print("h1 is :", soup.h1)
