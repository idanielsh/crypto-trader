from abc import ABC, abstractmethod

import pandas as pd

class AbstractMarket(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def buy(self, price):
        raise NotImplementedError()

    @abstractmethod
    def buy(self, price):
        raise NotImplementedError()

    @abstractmethod
    def get_buy_price(self):
        raise NotImplementedError()

    @abstractmethod
    def get_sell_price(self):
        raise NotImplementedError()

    @abstractmethod
    def get_new_market_data() -> pd.DataFrame:
        raise NotImplementedError()

