# on tuple
tp = (12.2, "a")
print(tp[1])


import requests
from bs4 import BeautifulSoup as bs
#
response = requests.get('https://www.baidu.com/')
print(response.encoding)
response.encoding = 'utf-8'
html = response.text
print(html)
print(response.status_code)
print(type(response.text))
print("中文")

soup = bs(html, 'html.parser')
print(soup.find_all('a'))

