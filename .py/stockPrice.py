import sys
from bs4 import BeautifulSoup
import requests

try:
    r = requests.get('https://finance.yahoo.com/quote/{}'.format(sys.argv[1]))
    soup = BeautifulSoup(r.content, parser='html-parser', features='lxml')
    text = soup.find("div", attrs={"data-reactid": "28"})
    price = text.find("span", attrs={"data-reactid": "32"}).get_text()
    change = text.find("span", attrs={"data-reactid": "33"}).get_text()
    print("{}: {}{}".format(sys.argv[1], price, change))

except AttributeError:
    print("Error: Ticker {} cannot be found".format(sys.argv[1]))

except IndexError:
    print("Error: No ticker entered")
