from enum import Enum


# 붕어빵의 종류는 겹칠 수 없음
class PersonAuthority(Enum):
    CEO = "대표"
    STORE_OWNER = "가게 주인"
    STORE_MANAGER = "가게 매니저"
    CUSTOMER = "손님"

    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self):
        return self._name
