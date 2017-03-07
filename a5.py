import requests
from bs4 import BeautifulSoup
import re

baseurl = 'http://'

target_url = 'http://' 
r = requests.get(target_url) 
soup = BeautifulSoup(r.text, 'lxml') 

price = []
xxx =  soup.select('#newBookList > ul > li > div.data > p.price')
for x in xxx:
	price.append(x.string)

xx =  soup.select('#newBookList > ul > li > div.cover > a > img')
books = len(xx)

title = []
for x in xx:
	title.append(x['title'])

for i in range(0, books):
	print ( title[i] + price[i] )
