# https://www.crummy.com/software/BeautifulSoup/

from bs4 import BeautifulSoup

import requests

url = 'https://www.crummy.com/software/BeautifulSoup'

r = requests.get(url)

html_doc = r.text

soup = BeautifulSoup(html_doc, "lxml")

print(soup.prettify())

print(soup.title)

print(soup.get_text())

for link in soup.find_all('a'):
    print(link.get('href'))

    