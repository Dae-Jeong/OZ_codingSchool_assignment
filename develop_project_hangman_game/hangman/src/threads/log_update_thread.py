from src.utils.queue_manager import game_message_queue
from PyQt5 import QtCore

import threading


class LogUpdateThread(threading.Thread):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    def run(self):
        while True:
            if game_message_queue:
                message = game_message_queue.popleft()
                self.main_window.update_game_log_text_box(message)
            else:
                QtCore.QThread.msleep(100)  # 큐에 값이 없으면 잠시 대기
