import requests
from bs4 import BeautifulSoup
import re

url = "https://www.biomedcentral.com/journals"
response = requests.get(url)

if response.status_code == 200:
    content = response.text
    # Do something with the content
else:
    print("Failed to fetch the URL, status code:", response.status_code)


# tag的相关应用
print('----------------------tag的相关应用---------------------')
soup = BeautifulSoup(content, "html.parser")
tag = soup.div
print(type(content))
print(type(tag))
print(tag.name)
print(tag.attrs)
print(tag.string)


# string和strings的应用
print('----------------------string和strings的应用---------------------')
soup2 = BeautifulSoup('<div class="body strikeout"><h2>hello world 1</h2><br/><h1><p>hello world 2</p><p>hello world 3</p></h1></div>',
                      "html.parser")
print(soup2.div.h2.string)
for string in soup2.div.strings:
    print(string)


# 遍历文档树
print('----------------------遍历文档树---------------------')
# print(soup.body.a)
# print(soup.body.find_all('a'))
# print(soup.head.contents)
print(soup.contents[2].name)
print(soup.body.children)
print(len(soup.body.contents))
# for child in soup.body.contents:
#     print(child)
print(soup2.contents)
print('----------------------.descendants---------------------')
# print(soup2.descendants)
# for child in soup2.descendants:
#     print(child)


# 父节点
print('----------------------父节点.parent---------------------')
print(soup2.p)
print(soup2.p.parent)
print(soup2.p.string.parent)
print('----------------------父节点.parents---------------------')
for parent in soup2.p.string.parents:
    print(parent)

# 前进和后退
print('----------------------前进和后退---------------------')
print(soup2.p.string.next_element)


# find_all
print('----------------------find_all text参数---------------------')
print(soup2.find_all(string=re.compile("hello")))
print('----------------------find_all recursive参数---------------------')
print(soup2.find_all("h1", recursive=False))
print(soup2.div.find_all("h1", recursive=False))

# css选择器
print('----------------------css选择器---------------------')
print(soup2.select("p:nth-of-type(2)"))
