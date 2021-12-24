import pandas as pd
import glob
from util import beautify_klines_df

path = r'/home/idanielsh/Documents/crypto-trading-app/crypto-trader/data/data/spot/daily/klines/ETHUSDT/15m' 
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=None)
    li.append(df)

df = pd.concat(li, axis=0, ignore_index=True)



df = beautify_klines_df(df)

print(df.head())
print(len(df))