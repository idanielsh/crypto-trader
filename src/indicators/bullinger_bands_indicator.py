from typing import Any, Tuple
import pandas as pd
from src.indicators.abstract_indicator import AbstracIndicator
from ta.volatility import BollingerBands



class BollingerBandsIndicator(AbstracIndicator):


    def __init__(self, window=20, window_dev=2) -> None:
        super().__init__()
        self.window = window
        self.window_dev = window_dev
        

    def evaluate(self, df: pd.DataFrame) -> Tuple[int, int, int]:
        indicator_bb = BollingerBands(close=df["Close"], window=self.window, window_dev=self.window_dev)

        df['bb_bbm'] = indicator_bb.bollinger_mavg()
        df['bb_bbh'] = indicator_bb.bollinger_hband()
        df['bb_bbl'] = indicator_bb.bollinger_lband()

        return df

