# 这个代码是用到正则匹配来搜索
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re #使用正则表达式的时候需要导入re这个库

# 如果包含中文，则需要解码
html = urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode('utf-8')

soup = BeautifulSoup(html,features="lxml")
#下面通过正则表达式匹配带有后缀为.jpg的img标签
img_links = soup.find_all("img",{"src":re.compile('.*?\.jpg')})
for link in img_links:
    print(link['src'])

#我只是一条分割线。。。
print('-'*100)

#下面用正则匹配找到开头为https://morvan的链接
course_links = soup.find_all('a',{'href':re.compile('https://morvan.*')})
for link in course_links:
    print(link['href'])
