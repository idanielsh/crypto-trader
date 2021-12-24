from abc import ABC, abstractmethod
import pandas as pd

from src.util import ACTION

class AbstractStrategy(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def get_action(self, price, df: pd.DataFrame) -> ACTION:
        raise NotImplementedError()


        


    