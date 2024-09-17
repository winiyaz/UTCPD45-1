#!/usr/bin/env python3 

import requests
from bs4 import BeautifulSoup

# Send a GET request to the page
response = requests.get("https://immunefi.com/bug-bounty/")

# Parse with Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract data as needed
data = soup.find_all('table', class_='desired-class')
for item in data:
    print(item.text)

# Write to HTML file
with open('im2.html', 'w') as f:
    f.write(soup.prettify())