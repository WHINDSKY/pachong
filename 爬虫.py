import requests
from lxml import etree

response=requests.get('https://www.baidu.com')
print(response.text)


