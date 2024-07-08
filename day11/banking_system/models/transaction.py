class Transaction:
    def __init__(self, transaction_type: str, amount: int, balance: int) -> None:
        """
        :param str transaction_type: 거래 유형을 나타내는 문자열 (예: "입금", "출금")
        :param int amount: 거래 금액을 나타내는 정수
        :param int balance: 거래 후 잔고를 나타내는 정수
        """

        self.transaction_type = transaction_type
        self.amount = amount
        self.balance = balance

    def __str__(self) -> str:
        """
        :return str:
        """
        return (f"거래 유형: {self.transaction_type}\t"
                f"거래 금액: {self.amount}\t"
                f"거래 잔고: {self.balance}")

    def to_tuple(self) -> tuple[str, int, int]:
        return self.transaction_type, self.amount, self.balance
    