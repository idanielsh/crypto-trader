from abc import ABC, abstractmethod
from typing import Any
import pandas as pd

class AbstractIndicator(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def evaluate(self, df: pd.DataFrame) -> Any:
        raise NotImplementedError()