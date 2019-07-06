#Web Scraper for SacredTexts.com
# Source - https://www.youtube.com/watch?v=7SWVXPYZLJM&t=397s
import requests
from bs4 import BeautifulSoup
5465
url = "http://www.sacred-texts.com/index.htm"
resp = requests.get(url)

#Ability to read the HTML in python
soup = BeautifulSoup(resp.text, 'html.parser')

# Find the names and links to the books in the website's menu elements
topicMenu = soup.select(".menutext")

#Extract topic names
for topic in topicMenu:
    print(topic.text.strip())