# Description
# 1. Merges files links_N.csv into one file "links.csv"
# 2. Merges files data_N.csv into one file "data.csv"

import pandas as pd

# Settings
LINKS_NUM = 3
DATA_NUM = 20
DIR = 'YOU_DIR'

# Merge **links csv** files
df_1 = pd.read_csv(f'{DIR}/links_1.csv', index_col=0)
df_2 = pd.read_csv(f'{DIR}/links_2.csv', index_col=0)
df_3 = pd.read_csv(f'{DIR}/links_3.csv', index_col=0)

print(df_1.shape, df_2.shape, df_3.shape)

df = pd.concat([df_1, df_2, df_3])
print(df.shape)

# Save dataset
file_path = f'{DIR}/links.csv'
df.to_csv(file_path, index=False)

# Merge **data csv** files
data_list = []
for i in range(DATA_NUM):
  df_i = pd.read_csv(f'{DIR}/data_{i}.csv', index_col=0)
  data_list.append(df_i)

df = pd.concat(data_list)
print(df.shape)

# Save dataset
file_path = f'{DIR}/data.csv'
df.to_csv(file_path, index=False)