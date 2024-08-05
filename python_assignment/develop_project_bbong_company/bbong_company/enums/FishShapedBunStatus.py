from enum import Enum


class FishShapedBunStatus(Enum):
    SOLD_OUT = "매진"
    SALE = "판매중"

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        return self._name
