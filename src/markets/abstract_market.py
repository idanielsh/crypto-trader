from abc import ABC, abstractmethod

import pandas as pd

class AbstractMarket(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def buy(self, num):
        raise NotImplementedError()

    @abstractmethod
    def sell(self, amount):
        raise NotImplementedError()

    @abstractmethod
    def get_buy_price(self):
        raise NotImplementedError()

    @abstractmethod
    def get_sell_price(self):
        raise NotImplementedError()

    @abstractmethod
    def get_new_market_data(self) -> pd.DataFrame:
        raise NotImplementedError()

