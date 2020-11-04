from bs4 import BeautifulSoup 
import requests

url = requests.get('https://es.wikipedia.org/wiki/Halloween?')
search = BeautifulSoup(url.content,'html.parser')
info = search.find_all('p')
finaltext = info[0].getText()
print(finaltext)
