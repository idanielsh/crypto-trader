import pandas as pd
from strategies.abstract_strategy import AbstractStrategy
from indicators.bullinger_bands_indicator import BollingerBandsIndicator
from util import ACTION

# Outperforms bearish markets, underperforms bullish markets
class BulingerBandsStrategy(AbstractStrategy):
    bullinger_bands_indicator: BollingerBandsIndicator

    def __init__(self) -> None:
        super().__init__()
        self.bullinger_bands_indicator = BollingerBandsIndicator(window=20, window_dev=2)

    def get_action(self, price, df: pd.DataFrame) -> ACTION:
        low, med, high = self.bullinger_bands_indicator.evaluate(df = df)
        if price < low:
            return ACTION.BUY
        if price > high:
            return ACTION.SELL
        return ACTION.HOLD