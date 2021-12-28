from abc import ABC, abstractmethod
import pandas as pd

from util import ACTION

class AbstractStrategy(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def get_action(self, price, purchase_price, df: pd.DataFrame) -> ACTION:
        raise NotImplementedError()


        


    
