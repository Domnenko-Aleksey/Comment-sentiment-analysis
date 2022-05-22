'''
Рarse reviews from the site "sravni.ru"
1. We get the url of the reviews from the pages, with the url address https://www.sravni.ru/banki/otzyvy/?page=num, where "num" is the page number
2. Save data in **csv** format, fields: id, url, bank, rating
3. Upload a file with links to reviews pages
4. Open the page with reviews, parse the data
5. Save data in **csv** format
'''

# Import
import time
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Settings
PAGES_NUM = 1500  # Pages for parsing, 20 reviews per page
PART = 1  # Part of the downloaded data (STEP_PARTS), 500 pages
STEP_PARTS = 500  # downloading step
DIR = 'YOU_DIRECTORY'
URL = 'https://www.sravni.ru/banki/otzyvy/?page='  # Example: 'https://www.sravni.ru/banki/otzyvy/?page=1'

# Parsing
time_start = time.time()
data_list = []
part_start = (PART - 1)*STEP_PARTS + 1
part_end = part_start + STEP_PARTS + 1

for n in range(part_start, part_end):
  r = requests.get(URL + str(n))
  soup = BeautifulSoup(r.text, 'html.parser')

  # Iterate over the elements on the page and the available data
  items = soup.find_all("div", {"class": "sc-1fxln1u-15 dYgtcQ"})
  for item in items:
    rating_node = item.find_all("span", {"class": "sc-1eq8x10-0 fIgnKU"})
    if not rating_node:
      continue

    rating = rating_node[0].string
    span = item.find_all("span", {"class": "sc-1fxln1u-27 cPAIqy"})[0]
    link = span.a['href']
    link_list = link.split('/')
    bank = link_list[2]
    id = link_list[4]
    row = [id, link, bank, rating]
    data_list.append(row)

  time_delta = round(time.time() - time_start)
  if n % 10 == 0:
    print(f'Page num: {n}, time: {time_delta} s.')

# Save dataset
df = pd.DataFrame(data_list)
df.columns = ['id', 'link', 'bank', 'rating']

file_path = f'{DIR}/links_{PART}.csv'
df.to_csv(file_path)