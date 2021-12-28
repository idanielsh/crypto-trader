import pandas as pd
from strategies.abstract_strategy import AbstractStrategy
from indicators.bullinger_bands_indicator import BollingerBandsIndicator
from util import ACTION

# Performs very well when the market is decreasing. Does not perform well when
# the market is doing well
class GreedyStrategy(AbstractStrategy):
    bullinger_bands_indicator: BollingerBandsIndicator

    def __init__(self) -> None:
        super().__init__()
        self.bullinger_bands_indicator = BollingerBandsIndicator(window=20, window_dev=2)

    def get_action(self, price, purchase_price, df: pd.DataFrame) -> ACTION:
        low, med, high = self.bullinger_bands_indicator.evaluate(df = df)
        max_gain = 1.5
        max_loss = 0.95

        if price < low:
            return ACTION.BUY
        if purchase_price and (price > high or price > purchase_price*max_gain or price < purchase_price*max_loss):
            return ACTION.SELL
        return ACTION.HOLD
