from typing import Any, Tuple
import pandas as pd
pd.options.mode.chained_assignment = None
from indicators.abstract_indicator import AbstracIndicator
from ta.volatility import BollingerBands



class BollingerBandsIndicator(AbstracIndicator):


    def __init__(self, window=20, window_dev=2) -> None:
        super().__init__()
        self.window = window
        self.window_dev = window_dev
        

    def evaluate(self, df: pd.DataFrame) -> Tuple[int, int, int]:
        df = df.iloc[-20:]
        
        indicator_bb = BollingerBands(close=df['close'], window=self.window, window_dev=self.window_dev)

        df['bb_bbl'] = indicator_bb.bollinger_lband()
        df['bb_bbm'] = indicator_bb.bollinger_mavg()
        df['bb_bbh'] = indicator_bb.bollinger_hband()

        return (df.iloc[-1]['bb_bbl'], df.iloc[-1]['bb_bbm'], df.iloc[-1]['bb_bbh']) 

