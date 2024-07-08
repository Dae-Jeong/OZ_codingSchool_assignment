from models.user import User
from utils.exceptions import UserNotFoundError
from utils.input import input_int


class BankingService:
    def __init__(self) -> None:
        """
        users: 사용자 목록을 저장하는 리스트
        """
        self.users = []

    def add_user(self, username: str) -> None:
        """
        사용자를 추가하는 기능

        :param str username: 추가할 사용자의 이름
        """
        self.users.append(User(username=username))

    def find_user(self, username: str) -> User:
        """
        사용자를 조회하는 기능

        :param str username: 조회에 활용할 사용자 이름 (동일하게 작성 필요)

        :return User user: 조회된 사용자 반환

        :raise UserNotFoundError: 조회된 사용자가 없을 경우 에러 발생
        """

        for user in self.users:
            if user.username == username:
                return user

        # 유저를 찾지 못하면 Exception
        raise UserNotFoundError(username=username)

    def user_menu(self, username: str) -> None:
        """
        사용자가 은행 업무를 수행할 수 있는 기능 제공\n
        모드 : 입금, 출금, 잔고확인, 거래내역확인

        :param str username: 업무를 수행할 사용자 이름
        """
        user = self.find_user(username=username)
        print(f"안녕하세요 {username}님")

        while True:
            mode = input("활용하실 모드를 선택해주세요 [입금, 출금, 잔고확인, 거래내역확인, 종료] : ")

            if mode == "종료":
                break

            elif mode == "입금":
                while True:
                    amount = input_int("입금하실 금액을 정수로 입력하세요 : ")
                    try:
                        user.account.deposit(amount=amount)
                        break
                    except Exception as e:
                        print(e)

            elif mode == "출금":
                while True:
                    amount = input_int(f"출금하실 금액을 정수로 입력하세요 [잔고 : {user.account.get_balance()}원] : ")
                    try:
                        user.account.withdraw(amount=amount)
                        break
                    except Exception as e:
                        print(e)

            elif mode == "잔고확인":
                print(f"{username}님의 잔고는 {user.account.get_balance()}원 입니다.")

            elif mode == "거래내역확인":
                transactions = user.account.get_transactions()
                print(transactions)

            else:
                print("일치하는 모드가 없습니다. 다시 입력해주세요")

        print("모드가 종료되었습니다.")

