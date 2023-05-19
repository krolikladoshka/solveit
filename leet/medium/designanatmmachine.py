from typing import List


class ATM:
    def __init__(self):
        self.values = (
            20, 50, 100, 200, 500,
        )
        self.denominations = [
            0, 0, 0, 0, 0
        ]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, banknote_count in enumerate(banknotesCount):
            self.denominations[i] += banknote_count

    def withdraw(self, amount: int) -> List[int]:
        result = [0, 0, 0, 0, 0]
        denominations = enumerate(zip(self.values[:], self.denominations[:]))

        for i, (banknote_value, banknotes_count) in reversed(list(denominations)):
            min_amount = min(banknotes_count, amount // banknote_value)
            result[i] = min_amount
            amount -= min_amount * banknote_value

        if amount:
            return [-1]

        self.deposit(map(lambda x: -x, result))

        return result
