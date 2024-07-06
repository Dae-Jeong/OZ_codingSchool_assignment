from src.utils.queue_manager import hangman_image_queue
from PyQt5 import QtCore

import threading


class ImageUpdateThread(threading.Thread):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    def run(self):
        # 이 로직 수정하면 될 듯
        while True:
            if hangman_image_queue:
                image_url = hangman_image_queue.popleft()
                self.main_window.update_hangman_image(image_url)
            else:
                QtCore.QThread.msleep(100)  # 큐에 값이 없으면 잠시 대기
