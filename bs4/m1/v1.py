#!/usr/bin/env python3 

import requests
from bs4 import BeautifulSoup

url = "https://www.mksecrets.net/index.php?section=mk4&lang=eng&contentID=5982&title=Mortal-Kombat-4"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Write the HTML content to a file
with open('panty.html', 'w') as f:
    f.write(soup.prettify())