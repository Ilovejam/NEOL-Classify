
import pandas as pd

df = pd.read_excel('CohortDB.ods', engine='odf')

row_1=df.iloc[0]
print(row_1)