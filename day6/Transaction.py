class Transaction:
    def __init__(self, transaction_type: str, money: int, balance: int) -> None:
        self.transaction_type = transaction_type
        self.money = money
        self.balance = balance

    def __str__(self) -> str:
        return "거래 기록 : [{0}, {1}, {2}]".format(self.transaction_type, self.money, self.balance)

    def to_tuple(self) -> tuple[str, int, int]:
        return self.transaction_type, self.money, self.balance
