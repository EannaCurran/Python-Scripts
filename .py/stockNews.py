import sys
from bs4 import BeautifulSoup
import requests

try:
    r = requests.get('https://news.google.com/search?q={}+stock%20stock&hl=en-IE&gl=IE&ceid=IE%3Aen'.format(sys.argv[1]))
    soup = BeautifulSoup(r.content, features="lxml")
except Exception as e:
    print(e)
