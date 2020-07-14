import sys
from bs4 import BeautifulSoup
import requests

r = requests.get('https://finance.yahoo.com/quote/{}'.format(sys.argv[1]))
soup = BeautifulSoup(r.content, parser='html-parser', features='lxml')
list = soup.find(id='quote-header-info')
print(list.prettify())