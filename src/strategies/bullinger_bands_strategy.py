import pandas as pd
from src.strategies.abstract_strategy import AbstractStrategy
from src.indicators.bullinger_bands_indicator import BollingerBandsIndicator
from src.util import ACTION


class BulingerBandsStrategy(AbstractStrategy):
    bullinger_bands_indicator: BollingerBandsIndicator

    def __init__(self) -> None:
        super().__init__()
        self.bullinger_bands_indicator = BollingerBandsIndicator

    def get_action(self, price, df: pd.DataFrame) -> ACTION:
        print(self.bullinger_bands_indicator.evaluate(df))