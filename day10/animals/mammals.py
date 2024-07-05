
class Dog:
    def __init__(self, type: str) -> None:
        self.type = type

    def __str__(self) -> str:
        return f"이 개는 {self.type}타입 입니다."