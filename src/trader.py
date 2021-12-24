import pandas as pd

from src.state import State
from src.strategies.abstract_strategy import AbstractStrategy
from src.util import ACTION


class Trader:
    state: State
    historical_data: pd.DataFrame
    strategy: AbstractStrategy

    def __init__(self, money: int, historical_data: pd.DataFrame, 
        strategy: AbstractStrategy
        ) -> None:
        self.state = State(cash=money, crypto_owned=0)
        self.historical_data = historical_data
        self.strategy = strategy

    def make_desicion(self, price):
        if self.strategy.get_action(price=price, df = self.historical_data) == ACTION.BUY:
            self.buy(price)
        elif self.strategy.get_action(price=price, df = self.historical_data) == ACTION.SELL:
            self.sell(price)

    def update_historical_data(self, new_data: pd.DataFrame):
        self.historical_data = self.historical_data.append(new_data, ignore_index=True)

    def buy(self, price):
        pass

    def sell(self, price):
        pass

    





