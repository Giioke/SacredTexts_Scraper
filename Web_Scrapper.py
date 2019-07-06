#Web Scraper for SacredTexts.com
# Source - https://www.youtube.com/watch?v=7SWVXPYZLJM&t=397s
import requests
from bs4 import BeautifulSoup
5465
url = "http://www.sacred-texts.com/index.htm"
resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'html.parser')
print(soup)