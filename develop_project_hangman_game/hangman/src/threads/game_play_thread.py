from src.models.game.hangman_game import HangmanGame
import threading


class GamePlayThread(threading.Thread):
    """
    HangmanGame을 실행하는 백그라운드 스레드 클래스입니다.
    이 스레드는 HangmanGame 객체를 생성하고, 게임을 실행합니다.
    """

    def __init__(self):
        """
        GamePlayThread의 초기화 메서드입니다.
        """
        super().__init__()
        self.game = HangmanGame()  # 게임 객체 생성

    def run(self) -> None:
        """
        스레드의 메인 실행 메서드입니다.
        HangmanGame 객체의 play 메서드를 호출하여 게임을 실행합니다.

        :return
        """
        self.game.play()
