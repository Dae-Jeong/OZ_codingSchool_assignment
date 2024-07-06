from ..company.Company import Company
from ..company.BbongStore import BbongStore
from ..person.Person import StoreOwner, CEO

import datetime


# Company의 경우 Factory 아키텍처 공부해서 활용 / Store를 직접 생성은 X 무조건 Company를 통해서만 생성
class BbongCompany(Company):
    """
    붕 컴퍼니
    """

    def __init__(self, ceo: CEO, region: str, founded_dt: datetime):
        super().__init__(
            owner=ceo,
            region=region
        )
        self._store_list = list[BbongStore]()
        self._founded_dt = founded_dt

    def publish_store(self, store_owner: StoreOwner, region: str) -> BbongStore:
        store = BbongStore(
            store_owner=store_owner,
            region=region,
            founded_dt=datetime.datetime.now()
        )
        self._store_list.append(store)
        return store
