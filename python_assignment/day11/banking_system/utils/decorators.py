from utils.exceptions import NegativeAmountError, InsufficientFundsError
from typing import Callable


def validate_amount(amount: int) -> bool:
    """
    거래 금액의 유효성 검사를 수행하는 메서드

    :param int amount: 거래 금액

    :return bool: 금액이 0 이상이면 True, 음수면 False를 반환

    :raise TypeError: int가 아닌 다른 타입이 들어왔을 경우
    :raise NegativeAmountError: 금액이 음수로 들어왔을 경우
    """

    if amount < 0:
        if int == type(amount):  # float도 허용하지 않음
            raise NegativeAmountError(message="돈은 음수일 수 없습니다.")
        else:
            raise TypeError("잔고를 수정하는데에는 정수값이 필요합니다.")
    return True


# validate_transaction 기능으로 인해 사용 X
#
# def validate_balance(old_balance: int, calculated_balance: int) -> bool:
#     """
#     잔고의 유효성 검사를 수행하는 메서드
#
#     :param int old_balance: 연산 전 계좌 잔액
#     :param int calculated_balance: 연산 후 계좌 잔액
#
#     :return bool: 잔액이 0 이상이면 True를 반환
#
#     :raise InsufficientFundsError: 출금 금액이 잔고보다 클 경우
#     """
#
#     if calculated_balance < 0:
#         raise InsufficientFundsError(balance=old_balance, message="잔고보다 큰 금액을 찾을 수 없습니다.")
#
#     return True
#
#
# def validate_is_int(function: Callable[..., str]) -> Callable[..., bool]:
#     """
#     사용자가 입력한 입력 값이 int로 변환이 가능한지 체크하는 메서드
#
#     :return bool: int로 변환 가능하면 True, 아니면 False 반환
#     """
#     def wrapper(*args, **kwargs):
#         user_input = function(*args, **kwargs)
#         return user_input.isdigit()
#
#     return wrapper


def validate_transaction(function: Callable[..., int]) -> Callable[..., int]:
    """
    잔고의 유효성 검사를 수행하는 메서드

    :return Callable[..., int]: 출금 후 잔액 연산 결과 반환

    :raise InsufficientFundsError: 출금 금액이 잔고보다 클 때, 발생하는 에러
    """
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)

        if result < 0:
            raise InsufficientFundsError(balance=result, message="잔고보다 큰 금액을 찾을 수 없습니다.")

        return result

    return wrapper
