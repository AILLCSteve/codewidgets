'''to scour bs readout and find tag locs'''

import requests
from bs4 import BeautifulSoup
import pandas as pd 
import numpy as np 
import sqlite3
import datetime

table_attribs = ['Name','MC_USD_Billion']
url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
page = requests.get(url).text
data = BeautifulSoup(page, 'html.parser')
df = pd.DataFrame(columns = table_attribs)
tables = data.find_all('tbody')

# Write the prettified HTML to a file
dump_path = 'bs_dump.txt'
with open(dump_path, 'w', encoding='utf-8') as f:
    f.write(data.prettify())

print(f"Saved BeautifulSoup dump to: {dump_path}")