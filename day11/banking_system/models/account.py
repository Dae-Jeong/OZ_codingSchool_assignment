from utils import validate_amount, validate_transaction
from models.transaction import Transaction


class Account:
    """
    bank_name: 은행 이름을 나타내는 클래스 변수 문자열
    """
    bank_name = None

    def __init__(self) -> None:
        """
        __balance: 계좌 잔고를 나타내는 프라이빗 정수 변수
        transactions: 거래 내역을 저장하는 리스트
        amount: 입금 또는 출금 금액을 나타내는 정수
        """
        self.__balance = 0
        self.transactions = []

    def deposit(self, amount: int) -> None:
        """
        계좌 잔고에 돈을 입금하는 메서드
        :param int amount: 입금 또는 출금 금액을 나타내는 정수
        """
        def add_money():
            """
            돈을 입금하는 메서드
            """
            self.__balance += amount

        if not validate_amount(amount=amount):
            return

        add_money()
        self.__record_transaction(
            transaction_type="입금",
            amount=amount
        )

        print(f"입금이 완료되었습니다. 현재 잔액은 {self.get_balance()}원 입니다.")

    def withdraw(self, amount: int) -> None:
        """
        계좌 잔고에 돈을 출금하는 메서드
        :param int amount: 입금 또는 출금 금액을 나타내는 정수
        """

        @validate_transaction
        def reduce_money() -> int:
            """
            돈을 출금하는 메서드
            :return int:
            """

            return self.__balance - amount

        if not validate_amount(amount=amount):
            return

        self.__balance = reduce_money()
        self.__record_transaction(
            transaction_type="출금",
            amount=amount
        )
        print(f"출금이 완료되었습니다. 현재 잔액은 {self.get_balance()}원 입니다.")

    def get_balance(self) -> int:
        """
        잔액을 반환받는 메서드

        :return int: 계좌의 잔고를 반환
        """

        return self.__balance

    def get_transactions(self) -> list[Transaction]:
        """
        거래 내역을 반환하는 메서드

        :return list[tuple[str, int, int]]: 거래 내역 리스트를 반환
        """
        return self.transactions

    def __record_transaction(self, transaction_type: str, amount: int) -> None:
        """
        거래 기록을 남기는 메서드
        (논리적으로 금액에 대한 유효성 검사를 마친 amount값만 들어오기 때문에, 추가 유효성검사 X)

        :param str transaction_type: 출금, 입금의 거래 타입을 지정
        :param int amount: 거래 금액
        """

        self.transactions.append(
            Transaction(
                transaction_type=transaction_type,
                amount=amount,
                balance=self.__balance
            )
        )

    @classmethod
    def get_bank_name(cls) -> str | None:
        """
        bank_name을 반환받는 메서드

        :return str | None: 값이 지정되었으면 str, 그렇지 못하면 None을 반환
        """
        return cls.bank_name

    @classmethod
    def set_bank_name(cls, name: str) -> None:
        """
        bank_name을 수정하는 클래스 메서드
        """
        cls.bank_name = name
