from ..person.Person import Person, CEO, StoreOwner, StoreManager
from ..Balance import Balance
import datetime


class Company:
    def __init__(self, owner: Person, region: str):
        self._owner = owner
        self._region = region
        self._balance = Balance()






