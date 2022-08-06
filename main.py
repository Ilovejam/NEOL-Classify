from itertools import groupby
import pandas as pd
import matplotlib.pyplot as plt
import csv
import re
import nltk
from tqdm import tqdm

df = pd.read_excel('CohortDB.ods', engine='odf')
#print(df.head())

dataframe = df.values.tolist()

df_describe = []
for i in df['Which of the following describes you better?']:
  #print(i)
  df_describe.append(i)

# print(df_describe)
frequent_list = pd.DataFrame({'freq' : df_describe})
frequent_list.groupby('freq', as_index=False).size().plot(kind='bar')
plt.show()