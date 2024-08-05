import threading


class EventManager:
    """
    thread event 객체
    """

    def __init__(self) -> None:
        self.event = threading.Event()

    def set_event(self) -> None:
        """
        event를 set 상태로 변경합니다.
        :return:
        """
        self.event.set()

    def clear_event(self) -> None:
        """
        event의 상태를 초기화합니다.
        :return:
        """
        self.event.clear()

    def wait_for_event(self) -> None:
        """
        event를 대기 상태로 변경합니다.
        :return:
        """
        self.event.wait()


# 전역 인스턴스 생성
user_input_event_manager = EventManager()
# game_message_event_manager = EventManager()
life_update_event_manager = EventManager()
