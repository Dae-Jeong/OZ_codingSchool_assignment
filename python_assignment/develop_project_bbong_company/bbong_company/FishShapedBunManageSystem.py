from .enums.FishShapedBunStatus import FishShapedBunStatus as BunStatus
from .enums.FishShapedBunType import FishShapedBunType as BunType
from .validation import check_count


class FishShapedBunInventory:
    def __init__(self, bun_type: BunType, count: int, status: BunStatus):
        self._bun_type = bun_type.name
        self._count = count
        self._status = status

    @property
    def count(self):
        return self._count

    @property
    def status(self):
        return self._status

    @property
    def name(self):
        return self._bun_type

    def print_inventory(self):
        print("붕어빵 종류 : {0}, 붕어빵 잔여 개수 : {1}개, 현재 판매 상태 : {2}".format(
            self._bun_type,
            self._count,
            self._status.value
        ))

    def update_status(self) -> None:
        if self._status == BunStatus.SALE:
            self._status = BunStatus.SOLD_OUT
        else:
            self._status = BunStatus.SALE

    def add_buns(self, count: int) -> None:
        check_count(count)
        self._count += count

    def reduce_buns(self, count: int) -> None:
        check_count(count)
        self._count -= count

        # self._count == 0 과 같은 의미
        if not self._count:
            self.update_status()


class FishShapedBunManagedSystem:
    def __init__(self):
        self._bun_inventory = dict()
        self.__post_construct()

    def __post_construct(self):
        # for bun_type in FishShapedBunType:
        #     self._bun_inventory[bun_type.name] = FishShapedBunInventory(
        #         bun_type=bun_type,
        #         count=10,
        #         status=FishShapedBunStatus.SALE
        #     )

        self._bun_inventory[BunType.RED_BEAN.name] = FishShapedBunInventory(
            bun_type=BunType.RED_BEAN,
            count=10,
            status=BunStatus.SALE
        )

        self._bun_inventory[BunType.PUFF.name] = FishShapedBunInventory(
            bun_type=BunType.PUFF,
            count=8,
            status=BunStatus.SALE
        )

        self._bun_inventory[BunType.CHOCO.name] = FishShapedBunInventory(
            bun_type=BunType.CHOCO,
            count=5,
            status=BunStatus.SALE
        )

    @property
    def bun_inventory(self):
        return self._bun_inventory

    def print_inventories(self):
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        print("현재 관리중인 붕어빵 리스트 입니다.")
        for inventory in self._bun_inventory.values():
            inventory.print_inventory()
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")

    def add(self, bun_type: str, count: int):
        # TODO : 사용자 auth에 따라 적용 가능 여부 판단
        bun_inventory = self._bun_inventory.get(bun_type)
        bun_inventory.add_buns(count)
        print("[재고 추가] 종류 : {0}  | 추가 개수 : {1} | 재고 : {2}".format(
            bun_type, count, self._bun_inventory.get(bun_type).count))

    def reduce(self, bun_type: str, count: int):
        # TODO : 구매자에 따라서 할인율 적용 기능 필요
        bun_inventory = self._bun_inventory.get(bun_type)
        bun_inventory.reduce_buns(count)
