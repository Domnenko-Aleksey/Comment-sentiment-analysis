# Parsing review pages. Links are taken from the links.csv file

import time
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Settings
START_IDX = 0
BATCH = 1000 
DIR = 'YOU_DIRECTORY'

# Load links data
df = pd.read_csv(f'{DIR}/links.csv')

# Parsing
time_start = time.time()
data_list = []

for i in range(START_IDX, START_IDX+BATCH):
  if i >= df.shape[0]:
    break

  link = 'https://sravni.ru' + df.loc[i, 'link']
  r = requests.get(link)
  soup = BeautifulSoup(r.text, 'html.parser')
  item = soup.find_all("div", {"class": "sc-lpzn2g-9 bHspFi"})[0]

  id = int(df.loc[i, 'id'])
  title = item.find_all("h1", {"sc-lpzn2g-11 ljWdwX"})[0].string
  text_body = item.find_all("div", {"sc-lpzn2g-13 eCTrNq"})[0].getText()
  text = (title + ' ' + text_body.replace('\n', ''))
  r_5 = int(df.loc[i, 'rating'])
  bank = df.loc[i, 'bank']
  rating = 1  # 0, 1, 2
  if r_5 < 3:
    rating = 0
  if r_5 > 3:
    rating = 2

  row = [id, text, bank, rating]
  data_list.append(row)

  time_delta = round(time.time() - time_start)
  if i % 50 == 0:
    print(f'Comment idx: {i}, time: {time_delta} s.')

# Save dataset
df = pd.DataFrame(data_list)
df.columns = ['id', 'text', 'bank', 'rating']

n = int(START_IDX / BATCH)

file_path = f'{DIR}/data_{n}.csv'
df.to_csv(file_path)