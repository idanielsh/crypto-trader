
import pandas as pd
from util import ACTION

from strategies.bullinger_bands_strategy import BulingerBandsStrategy
from strategies.macd_strategy import MACDStrategy

# Strategy didn't work great
class EnsembleStrategy:
    def __init__(self):
        self.macd_strategy = MACDStrategy()
        self.bullinger_bands_strategy = BulingerBandsStrategy()

    def get_action(self, price, df: pd.DataFrame) -> ACTION:
        macd = self.macd_strategy.get_action(price, df)
        bb = self.bullinger_bands_strategy.get_action(price, df)

        if bb is macd:
            return bb

        return ACTION.HOLD