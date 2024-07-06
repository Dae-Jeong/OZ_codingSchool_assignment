import threading


class EventManager:
    def __init__(self):
        self.event = threading.Event()

    def set_event(self):
        self.event.set()

    def clear_event(self):
        self.event.clear()

    def wait_for_event(self):
        self.event.wait()


# 전역 인스턴스 생성
user_input_event_manager = EventManager()
# game_message_event_manager = EventManager()
life_update_event_manager = EventManager()