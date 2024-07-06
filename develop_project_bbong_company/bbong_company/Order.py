import datetime


class Transaction:
    def __init__(self, bun_type: str, count: int, price: int):
        self._bun_type = bun_type
        self._count = count
        self._price = price

    @property
    def bun(self) -> str:
        return self._bun_type

    @property
    def count(self) -> int:
        return self._count

    @property
    def price(self) -> int:
        return self._price


class Order:
    def __init__(self, transaction_list: list[Transaction]):
        self._transaction_list = transaction_list
        self._order_dt = datetime.datetime.now()

    @property
    def transaction_list(self):
        return self._transaction_list

    def get_total_price(self) -> int:
        total_price = 0

        for transaction in self._transaction_list:
            total_price += transaction.price * transaction.count

        return total_price

    def print_order(self) -> None:
        order_message = ""

        for transaction in self._transaction_list:
            order_message += "{0} {1}개 ".format(transaction.bun, transaction.count)

        print("[{0}] {1}가 주문되었습니다. / 총 결제 금액은 {2}원 입니다.".format(self._order_dt, order_message, self.get_total_price()))
