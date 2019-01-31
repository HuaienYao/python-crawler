from urllib.request import urlopen

# 如果有中文就解码
html = urlopen("https://huaien.me").read().decode('utf-8')
print(html)

#使用正则匹配title部分打印出来
import re
res = re.findall(r"<title>(.+?)</title>",html)
print("\nPage title is:",res[0])


# 匹配段落<p>
res = re.findall(r"<p>(.*?)</p>",html,flags = re.DOTALL)
print("\n Page paragraph is : ",res[0])

#匹配网页内的所有链接
res = re.findall(r'href="(.*?)"',html)
print("\nAll links:",res)
