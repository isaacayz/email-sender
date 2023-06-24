import wikipediaapi
import requests
from bs4 import BeautifulSoup

"""""
wiki = wikipediaapi.Wikipedia('en')
query = wiki.page('Sinking_of_the_titanic')
print('Page Exist %s' % query.exists())
#print(query.text)
"""

url = "https://en.wikipedia.org/wiki/Sinking_of_the_Titanic"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('table', class_='wikitable')
#for result in results:
print(results)