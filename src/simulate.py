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


# SETTINGS
initial_data_for_trader = 50
simulation_data = load_simulation_data(r'data/LUNAUSDT-15m-2021-Increasing' )
strategy = BulingerBandsStrategy()
market=SimulatedMarket(simulation_data,initial_data_for_trader)
trader = Trader(money=100, historical_data=simulation_data.iloc[:initial_data_for_trader], strategy=strategy, market=market)


# Iterates through data
for _ in range(len(simulation_data)-initial_data_for_trader+1):
    trader.make_desicion()
    trader.update_historical_data()


trader.sell(trader.state.crypto_owned)
print(trader.state.cash)








