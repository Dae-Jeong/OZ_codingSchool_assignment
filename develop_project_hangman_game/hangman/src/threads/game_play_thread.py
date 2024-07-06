from src.models.game.hangman_game import HangmanGame
import threading


class GamePlayThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.game = HangmanGame()  # 게임 객체 생성

    def run(self):
        self.game.play()
