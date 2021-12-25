import pandas as pd
import glob
from strategies.ensemble_strategy import EnsembleStrategy
from strategies.macd_strategy import MACDStrategy
from util import beautify_klines_df
import logging

from trader import Trader
from strategies.bullinger_bands_strategy import BulingerBandsStrategy
from markets.simulated_market import SimulatedMarket

def load_simulation_data(path):
    all_files = glob.glob(path + "/*.csv")
    li = []
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=None)
        li.append(df)

    df = pd.concat(li, axis=0, ignore_index=True)
    df = beautify_klines_df(df)
    df = df.sort_index()
    return df



# Logging Setup
logging.basicConfig(
    format='%(levelname)s - %(asctime)s - %(message)s', 
    datefmt='%d-%b-%y %H:%M:%S', 
    level=logging.INFO
    )
logging.info("Program boot")

simulation_data = load_simulation_data(r'data/LUNAUSDT-4h-2021-Increasing' )
strategy = BulingerBandsStrategy()
market=SimulatedMarket(simulation_data,50)

print(len(simulation_data))

trader = Trader(money=100, historical_data=simulation_data.iloc[:50], strategy=strategy, market=market)


for _ in range(2150):
    trader.make_desicion()
    trader.update_historical_data()


trader.sell(trader.state.crypto_owned)
print(trader.state.cash)








