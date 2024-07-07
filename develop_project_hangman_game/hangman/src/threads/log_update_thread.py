from src.utils.queue_manager import game_message_queue
from PyQt5 import QtCore

import threading


class LogUpdateThread(threading.Thread):
    """
    게임 로그 업데이트를 담당하는 스레드 클래스입니다.

    이 스레드는 게임 메시지 큐를 모니터링하고, 큐에 메시지가 있는 경우 메인 윈도우의 로그 텍스트 박스를 업데이트합니다.
    """

    def __init__(self, main_window):
        """
        LogUpdateThread의 초기화 메서드입니다.

        :param MainApplication main_window: 로그 업데이트를 수행할 메인 윈도우 객체
        """
        super().__init__()
        self.main_window = main_window

    def run(self):
        """
        스레드의 메인 실행 메서드입니다.

        게임 메시지 큐를 지속적으로 모니터링하며, 큐에 메시지가 있을 경우 이를 꺼내어 메인 윈도우의
        로그 텍스트 박스를 업데이트합니다. 큐에 값이 없으면 잠시 대기합니다.

        :return:
        """
        while True:
            if game_message_queue:
                message = game_message_queue.popleft()
                self.main_window.update_game_log_text_box(message)
            else:
                QtCore.QThread.msleep(100)  # 큐에 값이 없으면 잠시 대기
