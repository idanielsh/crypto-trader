import pandas as pd
from strategies.abstract_strategy import AbstractStrategy
from indicators.macd_indicator import MACDIndicator
from util import ACTION


# Strategy also didn't work great
class MACDStrategy(AbstractStrategy):
    macd_indicator: MACDIndicator

    def __init__(self) -> None:
        super().__init__()
        self.macd_indicator = MACDIndicator(window_slow = 26, window_fast = 12, window_sign = 9)

    def get_action(self, price, df: pd.DataFrame) -> ACTION:
        macd, macd_signal = self.macd_indicator.evaluate(df)
        if macd>macd_signal:
            return ACTION.BUY
        if macd<macd_signal:
            return ACTION.SELL
        