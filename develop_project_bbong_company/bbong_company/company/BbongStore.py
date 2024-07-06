from ..company.Company import Company
from ..person.Person import StoreOwner, StoreManager
from ..FishShapedBunManageSystem import FishShapedBunManagedSystem as ManagedSystem
from ..FishShapedBunSellingSystem import FishShapedBunSellingSystem as SellingSystem
import datetime


class BbongStore(Company):
    """
    붕어빵 가게
    """
    def __init__(self, store_owner: StoreOwner, region: str, founded_dt: datetime):
        super().__init__(
            owner=store_owner,
            region=region
        )
        self._founded_dt = founded_dt
        self.__manager_mode = False
        self.__manager_list = list[StoreManager]() # 직원 관리 시스템으로 별도 객체화 필요
        self.__bbong_manage_system = ManagedSystem()
        self.__bbong_selling_system = SellingSystem(self.__bbong_manage_system)

    def change_mode(self, manager: StoreManager | StoreOwner):
        """
        :Param
        manager: StoreManager | StoreOwner

        :Return
        None
        """

        if not isinstance(manager, StoreOwner):
            if manager not in self.__manager_list:
                raise PermissionError(f"{self._region} 지점의 매니저가 아니라면 실행할 수 없습니다.")

        if self.__manager_mode:
            input_value = input("모드를 종료 하시겠습니까? (종료를 원한다면 '종료'를 입력하세요) : ")
            if input_value == "종료":
                self.__manager_mode = False
            else:
                raise ValueError("잘못 입력하셨습니다. 모드 전환을 종료합니다.")
        else:
            input_value = input("모드를 실행 하시겠습니까? (실행을 원한다면 '살행'를 입력하세요) : ")
            if input_value == "실행":
                self.__manager_mode = False
            else:
                raise ValueError("잘못 입력하셨습니다. 모드 전환을 종료합니다.")
            self.__manager_mode = True

    def sell(self):
        while True:
            order = self.__bbong_selling_system.order()

            if not order:
                return

            for transaction in order.transaction_list:
                self.__bbong_manage_system.reduce(bun_type=transaction.bun, count=transaction.count)

            self.__bbong_selling_system.add_order_record(order)
            order.print_order()

            if input("계속해서 구매하시겠습니까? (종료를 원하신다면 '종료'라고 입력해주세요) :") == "종료":
                break

    def add_manager(self, owner: StoreOwner, manager: StoreManager):
        if not self.__manager_mode:
            raise PermissionError("관리 모드가 활성화되지 않았습니다.")

        # Auth
        if not isinstance(owner, StoreOwner):
            raise PermissionError("가게 주인이 아니면 접근할 수 없습니다.")

        if not isinstance(manager, StoreManager):
            raise PermissionError("가게 매니저가 아니라면 추가될 수 없습니다.")

        self.__manager_list.append(manager)
        print(f"{manager.name}님이 {self._region}지점 매니저로 추가되었습니다.")

    def add_stock(self):
        # Auth
        if not self.__manager_mode:
            raise PermissionError("관리 모드가 활성화되지 않았습니다.")

        while True:
            bun_type = input("추가하실 빵 종류를 입력하세요 (팥붕어빵, 슈크림붕어빵, 초코붕어빵) : ")
            count = int(input(f"추가하실 {bun_type}의 개수를 입력하세요 (정수만 입력하시오) : "))

            self.__bbong_manage_system.add(bun_type=bun_type, count=count)

            if input("계속해서 추가하시겠습니까? (종료를 원하신다면 '종료'라고 입력해주세요) :") == "종료":
                break

    def check_bun_inventory(self):
        if not self.__manager_mode:
            raise PermissionError("관리 모드가 활성화되지 않았습니다.")

        self.__bbong_manage_system.print_inventories()

    def check_order_record(self):
        if not self.__manager_mode:
            raise PermissionError("관리 모드가 활성화되지 않았습니다.")

        self.__bbong_selling_system.print_order_list()