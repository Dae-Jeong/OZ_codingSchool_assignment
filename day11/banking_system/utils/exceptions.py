class InsufficientFundsError(Exception):
    """
    출금 금액이 잔고보다 클 경우 발생하는 에러
    """

    def __init__(self, balance: int, message: str = "Insufficient funds"):
        self.balance = balance
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'{self.message}: {self.balance}'


class NegativeAmountError(Exception):
    """
    연산 금액이 음수일 경우 발생하는 에러
    """

    def __init__(self, message: str = "Amount cannot be negative"):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return self.message


class UserNotFoundError(Exception):
    """
    조회하는 사용자가 없을 경우 발생하는 에러
    """

    def __init__(self, username: str, message: str = "User not found"):
        self.username = username
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.username}'
