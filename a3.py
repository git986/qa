import requests
from bs4 import BeautifulSoup

target_url = 'http://'  
r = requests.get(target_url)         
soup = BeautifulSoup(r.text, 'lxml') 

xxx =  soup.select('dl > dd') 
for x in xxx:
	print(x.string)

