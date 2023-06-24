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
results = soup.find_all('a')
men = soup.find_all(string='Men')

for result in results:
    #print(result, end='\n')
    #table_head = result.find('tr')
    #table_body = result.find('tbody')
    links = result['href']
    print('Apply here ',links, '\n')
    #print(table_body)