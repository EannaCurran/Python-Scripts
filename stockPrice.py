import sys
from bs4 import BeautifulSoup
import requests

r = requests.get('https://finance.yahoo.com/quote/{}'.format(sys.argv[1]))
soup = BeautifulSoup(r.content, parser='html-parser', features='lxml')
price = soup.find("span", class_="Trsdu(0.3s)", attrs={"data-reactid": "14"}).get_text()
print(price)