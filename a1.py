import requests
from bs4 import BeautifulSoup

target_url = 'http://'  
r = requests.get(target_url)         
soup = BeautifulSoup(r.text, 'lxml') 

x = soup.head.title.string
print( x )





