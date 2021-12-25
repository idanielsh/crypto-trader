from typing import Any, Tuple
import pandas as pd
pd.options.mode.chained_assignment = None
from indicators.abstract_indicator import AbstractIndicator
from ta.trend import MACD



class MACDIndicator(AbstractIndicator):


    def __init__(self, window_slow: int = 26, window_fast: int = 12, window_sign: int = 9) -> None:
        super().__init__()
        self.window_slow = window_slow
        self.window_fast = window_fast
        self.window_sign = window_sign
        

    def evaluate(self, df: pd.DataFrame) -> Tuple[int, int]:
        df = df.iloc[-(self.window_slow+self.window_sign):]
        
        macd_trend = MACD(close=df['close'], window_fast=self.window_fast, window_sign=self.window_sign, window_slow=self.window_slow)

        df['macd'] = macd_trend.macd()
        df['macd_signal'] = macd_trend.macd_signal()
        

        return (df.iloc[-1]['macd'], df.iloc[-1]['macd_signal']) 

