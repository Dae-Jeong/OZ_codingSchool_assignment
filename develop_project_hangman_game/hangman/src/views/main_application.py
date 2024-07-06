from PyQt5.QtWidgets import QMainWindow
from src.ui import Ui_HangManGame
from src.threads import GamePlayThread, LogUpdateThread, ImageUpdateThread
from src.models.game.hangman_game import HANGMAN_BASE_IMG


class MainApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_HangManGame()
        self.game_play_thread = None
        self.log_update_thread = None
        self.image_update_thread = None

        self.ui.setup_ui(self)
        self.__init_game()

    def __init_game(self):
        self.ui.update_hangman_image(image_path=HANGMAN_BASE_IMG)

        # 게임 플레이 스레드 생성 및 실행
        self.game_play_thread = GamePlayThread()
        self.game_play_thread.start()

        # 로그 업데이트 스레드 생성 및 실행
        self.log_update_thread = LogUpdateThread(self.ui)
        self.log_update_thread.start()

        # 행맨 이미지 업데이트 스레드 생성 및 실행
        self.image_update_thread = ImageUpdateThread(self.ui)
        self.image_update_thread.start()



