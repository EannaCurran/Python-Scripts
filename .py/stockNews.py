import sys
from bs4 import BeautifulSoup
import requests
from textblob import TextBlob

try:
    r = requests.get(
        'https://news.google.com/search?q={}+stock%20stock&hl=en-IE&gl=IE&ceid=IE%3Aen'.format(sys.argv[1]))
    soup = BeautifulSoup(r.content, features="lxml")
    count = 0
    total = 0
    for headline in soup.find_all("h3"):
        sentence = (headline.text.strip())
        sentiment = TextBlob(sentence).sentiment.polarity
        count += 1
        total += sentiment
        print("{} {} ".format(sentence, sentiment))

except Exception as e:
    print(e)
