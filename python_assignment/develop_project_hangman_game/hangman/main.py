import sys
from src.views import MainApplication
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    window = MainApplication()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

"""
TODO LIST
1. message를 가져오는 작업을 백그라운드 threading 처리 하기
2. 값을 입력할 때, 

"""
