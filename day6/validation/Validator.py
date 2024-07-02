

def check_money(money: int):
    """
    돈은 음수일 수 없다
    """
    if money < 0:
        raise ValueError("돈은 음수일 수 없습니다. 양수로 입력해주세요")
