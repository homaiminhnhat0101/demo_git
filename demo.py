import pandas as pd 
import numpy as np 

path = "C:/Users/PhiLong Technology/OneDrive/Desktop/DA//Data/Tradin/Stock_FMCG/Hangtieudung.csv"
df = pd.read_csv(path)

df.head(5)
type(df.snapshot_date)

df.snapshot_date = pd.to_datetime(df.snapshot_date)
df.snapshot_date.dt.month

print('successful')



