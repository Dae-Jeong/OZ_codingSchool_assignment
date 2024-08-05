def input_int(input_message: str) -> int:
    """
    사용자가 입력한 값을 int로 변환하여 반환하는 메서드
    :param str input_message: input 메서드에 활용할 메시지
    :return int: 사용자 입력 값
    """

    while True:
        user_input = input(input_message)

        if user_input.isdigit():
            return int(user_input)

        print(f"정수 값을 입력하세요 {user_input}는 정수가 아닙니다.")