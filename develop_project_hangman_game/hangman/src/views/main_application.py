from PyQt5.QtWidgets import QMainWindow
from src.ui import Ui_HangManGame
from src.threads import GamePlayThread, LogUpdateThread, ImageUpdateThread
from src.models.game.hangman_game import HANGMAN_BASE_IMG


class MainApplication(QMainWindow):
    """
    MainApplication 클래스는 PyQt의 QMainWindow를 확장하여 GUI 애플리케이션을 생성합니다.
    백그라운드 스레드에서 전달된 메시지를 텍스트 박스에 표시합니다.

    메인 어플리케이션 화면을 띄우는 클래스
    ui 생성부를 분리하여 요소들을 구성
    메인 스레드를 포함 총 4개의 스레드로 구성됨
    1. (GamePlayThread) 게임 플레이용 스레드
    2. (LogUpdateThread) 게임 메시지 출력용 스레드
    3. (ImageUpdateThread) 행맨 이미지 업데이트용 스레드
    """
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_HangManGame()
        self.game_play_thread = None
        self.log_update_thread = None
        self.image_update_thread = None

        self.ui.setup_ui(self)
        self.__init_game()

    def __init_game(self) -> None:
        """
        게임 초기화 및 스레드 실행 메서드

        :return:
        """
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



