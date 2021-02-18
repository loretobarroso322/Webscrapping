import requests
import re
from bs4 import BeautifulSoup as bs

# '''
# To run code on Repl.it:
# 1. On the right, open the "Shell tab"
# 2. Install the dependencies:
#    pip3 install -r requirements.txt
# 3. To run the code, you will need to run the follow code after your changes:
#     python3 main.py
# '''


# Load the webpage content
r = requests.get("//https://www.youtube.com/results?search_query=binging+with+babish")

# Convert to a beautiful soup object
soup = bs(r.content, features="html5lib")

Pretty prints out our html
print(soup.prettify())



dddkdkdk
