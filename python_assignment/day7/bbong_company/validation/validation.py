def check_is_num(input_value: str) -> bool:
    try:
        int(input_value)
    except ValueError:
        raise ValueError("정수 값을 입력해주세요.")

    return True


def check_count(count: int) -> bool:
    if count <= 0:
        raise ValueError("0개 이하의 주문은 수행할 수 없습니다.")

    return True


def check_bun(input_value: str) -> bool:
    if input_value not in ["1", "2", "3"]:
        raise ValueError("1, 2, 3 중에 하나를 선택해주세요")

    return True
