#!/usr/bin/env python3 

import requests
from bs4 import BeautifulSoup
from rich import print as rprint

# Defining a function to run the extraction and writing 

def ext1():

    url = "https://www.mksecrets.net/index.php?section=mk4&lang=eng&contentID=5982&title=Mortal-Kombat-4"
    response = requests.get(url)

    mysoup = BeautifulSoup(response.content, 'html.parser')

    # Write the HTML content to a file
    with open('panty.html', 'w') as f:
        f.write(mysoup.prettify())
        
    print('Extracted !!!')
    
    
        
def ext2():

    url = "https://www.mksecrets.net/index.php?section=mk4&lang=eng&contentID=5982&title=Mortal-Kombat-4"
    response = requests.get(url)

    mysoup = BeautifulSoup(response.content, 'html.parser')
    
    # rprint(mysoup.prettify())
    extracted_elements = mysoup.find_all(name='a')
    # rprint(extracted_elements)
    
    headingz = [a.get('href') for a in mysoup.find_all(name='a')]
    rprint(headingz)
    
    # for a in extracted_elements:
    #     rprint(a.get("href"))
    
        
ext2()

