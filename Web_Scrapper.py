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
#print(topicMenu[1])
#Extract topic names
for topic in topicMenu:
    print(topic.text.strip())

#####
#Data Structure
topics = {
    "topic1": {
        "descript": "content",
        "topicLink": "weblink"
    },
    "topic2": {
        "descript": "content",
        "topicLink": "weblink"

    }
#Add more topics?
}
#####

#For-Loop each topic displays their name, description, and the link.
for topicname, topicinfo in topics.items():
    print("\n")
    print(topicname)
    print(topicinfo['descript'])
    print(topicinfo['topicLink'])
    print("\n")