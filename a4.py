import requests
from bs4 import BeautifulSoup
import re

baseurl = 'http://'

target_url = 'http://'
r = requests.get(target_url) 
soup = BeautifulSoup(r.text, 'lxml') 

for a in soup.find_all('a', href=re.compile("^http")):
	print(a.get('href'))

for a in soup.find_all('a', href=re.compile("^(?!http)")):
	print( baseurl + a.get('href'))


