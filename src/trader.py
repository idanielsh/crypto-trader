import pandas as pd
pd.options.mode.chained_assignment = None
from markets.abstract_market import AbstractMarket

from state import State
from strategies.abstract_strategy import AbstractStrategy
from util import ACTION


class Trader:
    state: State
    historical_data: pd.DataFrame
    strategy: AbstractStrategy
    market: AbstractMarket

    def __init__(self, money: int, historical_data: pd.DataFrame, 
        strategy: AbstractStrategy, market: AbstractMarket
        ) -> None:
        self.state = State(cash=money, crypto_owned=0)
        self.historical_data = historical_data
        self.strategy = strategy
        self.market = market

    def make_decision(self):
        buy_price = self.market.get_buy_price()
        sell_price = self.market.get_sell_price()

        buy_decision = self.strategy.get_action(price=buy_price, df = self.historical_data)
        sell_decision = self.strategy.get_action(price=sell_price, df = self.historical_data)

        if buy_decision is ACTION.BUY:
            self.buy(self.state.cash)
        elif sell_decision is ACTION.SELL:
            self.sell(self.state.crypto_owned)

    def update_historical_data(self):
        self.historical_data = self.historical_data.append(self.market.get_new_market_data(), ignore_index=True)

    def buy(self, cost):
        if self.state.cash > 0:
            self.state.crypto_owned = self.market.buy(cost)
            self.state.cash = 0
        

    def sell(self, amount):
        if self.state.crypto_owned > 0:
            self.state.cash = self.market.sell(amount)
            self.state.crypto_owned = 0

    





