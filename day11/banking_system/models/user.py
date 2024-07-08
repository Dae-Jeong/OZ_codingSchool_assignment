from models.account import Account


class User:
    def __init__(self, username: str) -> None:
        """
        username: 사용자의 이름을 나타내는 문자열
        account: 사용자의 계좌를 나타내는 Account 객체
        """

        self.username = username
        self.account = Account()
