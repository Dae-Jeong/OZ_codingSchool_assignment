from ..enums.PersonAuthority import PersonAuthority
from ..Balance import Balance

import datetime


class Person:
    # name : string / balance : Money / auth : PersonAuthority
    def __init__(self, name: str, auth: PersonAuthority) -> None:
        self._name = name
        self._auth = auth
        self._balance = Balance()

    def __str__(self):
        return "[{0}, {1}, {2}]\n".format(self._name, self._auth.name, self._balance)

    def __post_construct(self) -> None:
        # 모든 사람에게 기본적으로 10000원을 주고 시작
        self._balance.add_money(10000)
        print(f"잔액이 {self._balance}원으로 시작합니다.")

    @property
    def name(self):
        return self._name


class CEO(Person):
    def __init__(self, name: str, appointed_dt: datetime):
        super().__init__(
            name=name,
            auth=PersonAuthority.CEO
        )
        self._appointed_dt = appointed_dt


class StoreOwner(Person):
    def __init__(self, name: str, purchased_dt: datetime):
        super().__init__(
            name=name,
            auth=PersonAuthority.STORE_OWNER
        )
        self._purchased_dt = purchased_dt


class StoreManager(Person):
    def __init__(self, name: str, appointed_dt: datetime):
        super().__init__(
            name=name,
            auth=PersonAuthority.STORE_MANAGER
        )
        self._appointed_dt = appointed_dt


class Customer(Person):
    def __init__(self, name: str):
        super().__init__(
            name=name,
            auth=PersonAuthority.CUSTOMER
        )

