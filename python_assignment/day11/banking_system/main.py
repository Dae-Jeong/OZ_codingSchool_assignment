from services.banking_service import BankingService


def main(banking_service: BankingService):
    while True:
        username = input("당신의 이름을 적어주세요 (종료를 원하시면 '종료'를 입력하세요) : ")

        if username == "종료":
            break

        banking_service.user_menu(username=username)


if __name__ == "__main__":
    banking_service = BankingService()

    banking_service.add_user("김대정")
    banking_service.add_user("박대정")
    banking_service.add_user("이대정")
    banking_service.add_user("최대정")
    banking_service.add_user("송대정")

    main(banking_service=banking_service)
