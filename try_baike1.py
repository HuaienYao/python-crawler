#本代码是爬百度百科的小实验
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

#设置起始url
base_url = "https://baike.baidu.com"
his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]

url = base_url + his[-1]

html = urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html,features='lxml')
print(soup.find_all('h1').get_text(),'url:',his[-1])
