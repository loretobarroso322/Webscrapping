import requests
import re
from bs4 import BeautifulSoup as bs

# Load the webpage content
r = requests.get("//https://www.youtube.com/results?search_query=binging+with+babish")
print(r.content)
# Convert to a beautiful soup object
soup = bs(r.content, features="html5lib")

#Pretty prints out our html
print(soup.prettify())
