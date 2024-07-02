class Balance:
    # 추후에 화폐 단위 달러, 위안, 엔화 추가
    def __init__(self):
        self._balance = 0
        self._unit = "won"

    def add_money(self, money: int) -> None:
        # TODO : 들어오는 money에 대한 유효성 검사 진행 필요
        self._balance += money
