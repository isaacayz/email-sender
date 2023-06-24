import wikipediaapi
import requests

"""""
wiki = wikipediaapi.Wikipedia('en')
query = wiki.page('Sinking_of_the_titanic')
print('Page Exist %s' % query.exists())
#print(query.text)
"""

url = "https://en.wikipedia.org/wiki/Sinking_of_the_Titanic"
page = requests.get(url)

print(page.text)