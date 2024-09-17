#!/usr/bin/env python3

from firecrawl import FirecrawlApp
from rich import print as rprint

PANTY = "fc-6144cf220ff1463095539cf276dac2fd"

app = FirecrawlApp(api_key=PANTY)

# Mapping function 

import json

def map_web():
    try:
        map_result = app.map_url('https://firecrawl.dev')
        with open('fc.json', 'w') as f:
            json.dump(map_result, f)
        rprint(map_result)
    except Exception as e:
        rprint(f"Error: {e}")
# Execute function
map_web()