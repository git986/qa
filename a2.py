import requests
from bs4 import BeautifulSoup

target_url = 'http://'  
r = requests.get(target_url)         
soup = BeautifulSoup(r.text, 'lxml') 

count = 0
for dl in soup.find_all('dt'):
	count = count + 1

print( count )

