from enum import Enum
import pandas as pd
from datetime import datetime

class ACTION(Enum):
    HOLD = 0
    BUY = 1
    SELL = 2

def beautify_klines_df(df: pd.DataFrame):
    df.columns = ['open_time', 'open', 'high', 'low', 'close', 'vol',
     'close_time', 'quote_asset_vol', 'number_of_trades', 
     'taker_buy_base_asset_vol', 'taker_buy_quote_asset_vol', 'ignore']

    df = df[['open_time', 'open', 'high', 'low', 'close', 'vol', 'close_time']]

    df['open_time'] = df['open_time'].apply(lambda x: datetime.fromtimestamp(x/1000))
    df['close_time'] = df['close_time'].apply(lambda x: datetime.fromtimestamp(x/1000))

    df = df.set_index('open_time')

    return df


