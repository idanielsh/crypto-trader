from markets.abstract_market import AbstractMarket

import pandas as pd
from datetime import datetime
import logging

class SimulatedMarket(AbstractMarket):
    simulation_data: pd.DataFrame
    cur_datetime: datetime

    def __init__(self, simulation_data, start_index):
        super().__init__()
        self.simulation_data = simulation_data
        self.cur_datetime = simulation_data.iloc[start_index].name


    def buy(self, price):
        amount = price/self.simulation_data.loc[self.cur_datetime]['high']
        logging.info(f'Bought {amount} at {self.simulation_data.loc[self.cur_datetime]["high"]} for {price} on {self.cur_datetime}')
        return amount

    def sell(self, amount):
        price = self.simulation_data.loc[self.cur_datetime]['low']*amount
        logging.info(f'Sold {amount} at {self.simulation_data.loc[self.cur_datetime]["low"]} for {price} on {self.cur_datetime}')
        return price

    def get_buy_price(self):
        return self.simulation_data.loc[self.cur_datetime]['high']

    def get_sell_price(self):
        return self.simulation_data.loc[self.cur_datetime]['low']

    def get_new_market_data(self) -> pd.DataFrame:
        cur_row = self.simulation_data.index.get_loc(self.cur_datetime)
        new_market_data = self.simulation_data.iloc[cur_row+1]
        new_market_data['open_time'] = self.cur_datetime

        self.cur_datetime = new_market_data.name
        
        return new_market_data

