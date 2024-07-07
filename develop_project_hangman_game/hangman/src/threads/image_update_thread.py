import threading
from PyQt5 import QtCore
from src.utils.queue_manager import hangman_image_queue


class ImageUpdateThread(threading.Thread):
    """
    행맨 이미지를 업데이트하는 스레드 클래스입니다.

    이 스레드는 행맨 이미지 큐를 모니터링하고, 큐에 이미지 URL이 있는 경우 메인 윈도우의 행맨 이미지를 업데이트합니다.
    """

    def __init__(self, main_window):
        """
        ImageUpdateThread의 초기화 메서드입니다.

        :param MainApplication main_window: 행맨 이미지 업데이트를 수행할 메인 윈도우 객체
        """
        super().__init__()
        self.main_window = main_window

    def run(self) -> None:
        """
        스레드의 메인 실행 메서드입니다.

        행맨 이미지 큐를 지속적으로 모니터링하며, 큐에 이미지 URL이 있을 경우 이를 꺼내어 메인 윈도우의
        행맨 이미지를 업데이트합니다. 큐에 값이 없으면 잠시 대기합니다.

        :return:
        """
        while True:
            if hangman_image_queue:
                image_url = hangman_image_queue.popleft()
                self.main_window.update_hangman_image(image_url)
            else:
                QtCore.QThread.msleep(100)  # 큐에 값이 없으면 잠시 대기
