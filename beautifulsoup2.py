from bs4 import BeautifulSoup
from urllib.request import urlopen

# 如果包含中文就解码
html = urlopen("https://morvanzhou.github.io/static/scraping/list.html").read().decode('utf-8')
print(html)

soup = BeautifulSoup(html,features='lxml')

#使用class来搜索
month = soup.find_all('li',{"class":"month"})
for m in month:
    print(m.get_text())

jan = soup.find_all('ul',{'class':'jan'})
j_jan = jan.find_all('li') # 教程里面有这句代码，不知道什么意思，写了use jan as a parent，但是我没加这句也可以正常执行
for j in jan:
    print(j.get_text())
