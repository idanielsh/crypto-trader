from src.markets.abstract_market import AbstractMarket

import pandas as pd
from datetime import datetime

class SimulatedMarket(AbstractMarket):
    simulation_data: pd.DataFrame
    cur_datetime: datetime

    def __init__(self, simulation_data):
        super().__init__()
        self.simulation_data = simulation_data.set_index('open_time')
        self.cur_datetime = simulation_data.iloc[0]['open_time']


    def buy(self, price):
        return price/self.simulation_data[self.cur_datetime]['high']

    def sell(self, amount):
        raise self.simulation_data[self.cur_datetime]['low']*amount

    def get_buy_price(self):
        return self.simulation_data[self.cur_datetime]['high']

    def get_sell_price(self):
        return self.simulation_data[self.cur_datetime]['low']

    def get_new_market_data(self) -> pd.DataFrame:
        cur_row = self.simulation_data.get_loc(self.cur_datetime)
        new_market_data = self.simulation_data.get_iloc[:cur_row+2]
        self.cur_datetime = new_market_data.iloc[-1]['open_time']

        return new_market_data

