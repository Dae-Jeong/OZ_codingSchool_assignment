from enum import Enum


# 붕어빵의 종류는 겹칠 수 없음
class FishShapedBunType(Enum):
    RED_BEAN = ("팥붕어빵", 2000)
    PUFF = ("슈크림붕어빵", 2500)
    CHOCO = ("초코붕어빵", 3000)

    def __init__(self, name: str, price: int):
        self._name = name
        self._price = price

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> int:
        return self._price
