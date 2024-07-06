from .FishShapedBunManageSystem import FishShapedBunManagedSystem as ManagedSystem
from .validation import check_bun, check_count, check_is_num
from .enums.FishShapedBunStatus import FishShapedBunStatus as BunStatus
from .enums.FishShapedBunType import FishShapedBunType as BunType
from .Order import Order, Transaction


class FishShapedBunSellingSystem:
    def __init__(self, managed_system: ManagedSystem):
        self._managed_system = managed_system
        self._order_record = list[Order]()
        self._bun_menu = {
            1: BunType.RED_BEAN,
            2: BunType.PUFF,
            3: BunType.CHOCO
        }

    def __print_menu(self) -> None:
        inventory = self._managed_system.bun_inventory
        print("==============================")
        for value in inventory.values():
            print(f"[{value.status.value}] {value.name} : {value.count}개")
        print("==============================")

    def __choose_bun(self) -> BunType | None:
        print("구매하실 붕어빵을 선택해주세요")
        print(f"{BunType.RED_BEAN.name} : 1")
        print(f"{BunType.PUFF.name} : 2")
        print(f"{BunType.CHOCO.name} : 3")
        print("'종료' 를 입력하시면 종료됩니다.")
        input_value = input("어떤 붕어빵을 구매하시겠습니까? : ")

        if input_value == "종료":
            return None

        check_bun(input_value)
        check_is_num(input_value)

        return self._bun_menu.get(int(input_value))

    def __choose_count(self, bun_type: str) -> int:
        print(f"{bun_type}를 선택하셨습니다")

        # 남은 붕어빵 개수
        inventory = self._managed_system.bun_inventory
        bun_count = inventory.get(bun_type).count

        while True:
            input_value = input(f"구매하실 수량을 입력해주세요 [잔여수량 : {bun_count}개] : ")
            check_is_num(input_value)

            count = int(input_value)
            if count > bun_count:
                print("잔여수량보다 많은 개수는 입력할 수 없습니다.")
                continue

            check_count(count)
            return count

    def order(self) -> Order | None:
        transaction_list = list[Transaction]()

        print("현재 판매중인 붕어빵 메뉴를 표시합니다.")
        self.__print_menu()
        bun_type = self.__choose_bun()

        if self._managed_system.bun_inventory.get(bun_type.name).status == BunStatus.SOLD_OUT:
            print("선택하신 빵은 현재 재고가 없습니다.")
            return

        if not bun_type:
            print("구매를 종료합니다.")
            return

        count = self.__choose_count(bun_type.name)
        transaction = Transaction(
            bun_type=bun_type.name,
            count=count,
            price=bun_type.price
        )
        transaction_list.append(transaction)
        order = Order(transaction_list)

        return order

    def add_order_record(self, order):
        self._order_record.append(order)

    def print_order_list(self):
        total_price = 0
        print("===================================")
        print("금일 판매 기록입니다.")
        for order in self._order_record:
            order.print_order()
            total_price += order.get_total_price()
        
        print(f"금일 총 매출은 : {total_price}원 입니다.")
        print("===================================")
