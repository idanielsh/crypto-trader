
class State:
    def __init__(self, cash, crypto_owned) -> None:
        self.starting_amount = cash
        self.cash = cash
        self.crypto_owned = crypto_owned