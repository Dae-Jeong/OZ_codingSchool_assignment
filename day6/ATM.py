from Transaction import Transaction
from validation import check_money


class ATM:
    def __init__(self, username: str) -> None:
        self.balance = 0
        self.username = username
        self.transaction_records = list[tuple]()
        self.transaction_type_list = ['입금', '출금']

        self.__post_construct()

    def __post_construct(self) -> None:
        self.balance = 1000

    def __record_transaction(self, transaction_type: str, money: int) -> None:
        transaction = Transaction(
            transaction_type=transaction_type,
            money=money,
            balance=self.balance
        )
        self.transaction_records.append(transaction.to_tuple())

    """
    def __validate_money_and_return_integer_money(self, transaction_type: str, input_value: str) -> tuple[bool, int]:
        def check_deposit_money() -> None:
            if money < 0:
                raise ValueError("음수 값은 입력할 수 없습니다.")

        def check_withdraw_money() -> None:
            if money < 0:
                raise ValueError("음수 값은 입력할 수 없습니다.")
            elif money > self.balance:
                raise ValueError(f"잔고 이상의 금액은 출금할 수 없습니다. / 현재 잔고는 : {self.balance}원 입니다.")

        print(f"{input_value}원 입력하셨습니다.")
        print("입력값의 유효성 검사를 실행합니다.")

        money = None
        try:
            money = int(input_value)
        except ValueError:  # PEP8 E722 로 인해, Except 구문에는 명확한 Exception 을 작성하여 어떤 오류가 발생했는지 파악토록 함
            raise ValueError("숫자가 아닌 값은 입력할 수 없습니다.")

        if transaction_type == '입금':
            check_deposit_money()
        elif transaction_type == '출금':
            check_withdraw_money()
        else:
            raise ValueError("입금 혹은 출금 둘중 한가지 값만 활용해주세요")

        return True, money
    """

    def input_money(self, transaction_type: str) -> int:
        if transaction_type not in self.transaction_type_list:
            raise ValueError("입금 혹은 출금 둘중 한가지 값만 활용해주세요")

        while True:
            input_value = input(f"{transaction_type}하실 금액을 입력해주세요 : ")

            try:
                money = int(input_value)
            except ValueError:  # PEP8 E722 로 인해, Except 구문에는 명확한 Exception 을 작성하여 어떤 오류가 발생했는지 파악토록 함
                raise ValueError("숫자가 아닌 값은 입력할 수 없습니다.")
            else:
                break

        return money

    # deposit과 withdraw는 하나로 합치려했으나, 명확한 코드를 확보하기 위해 기능을 분리
    def deposit(self) -> None:
        transaction_type = "입금"
        money = self.input_money(transaction_type=transaction_type)

        check_money(money)
        self.balance += money
        self.__record_transaction(
            transaction_type=transaction_type,
            money=money
        )

    def withdraw(self) -> None:
        transaction_type = "출금"
        money = self.input_money(transaction_type=transaction_type)

        check_money(money)
        if money > self.balance:
            raise ValueError(f"잔고 이상의 금액은 출금할 수 없습니다. / 현재 잔고는 : {self.balance}원 입니다.")

        self.balance -= money
        self.__record_transaction(
            transaction_type=transaction_type,
            money=money
        )

    def print_balance(self):
        print(f"{self.username}님께서 보유하신 계좌의 현재 잔고는 {self.balance}원 입니다.")

    def print_records(self):
        print("{0}님의 영수증을 출력합니다.".format(self.username))
        print("======================================")
        for record in self.transaction_records:
            print(record)
        print("======================================")
