# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sources/main_application.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from src.utils import singleton, user_input_event_manager
from src.models.game.hangman_game import user_input_queue


@singleton
class Ui_HangManGame(object):
    def setup_ui(self, main_window: QMainWindow) -> None:
        """
        UI 초기화 메서드

        :param QMainWindow main_window: UI 설정을 수행 할 메인 어플리케이션
        :return:
        """

        main_window.setObjectName("HangManGame")
        main_window.resize(480, 640)
        main_window.setMinimumSize(QtCore.QSize(480, 640))
        main_window.setMaximumSize(QtCore.QSize(480, 640))
        main_window.setBaseSize(QtCore.QSize(480, 640))

        self.titleLabel = QtWidgets.QLabel(main_window)
        self.titleLabel.setEnabled(True)
        self.titleLabel.setGeometry(QtCore.QRect(0, 0, 480, 70))

        font = QtGui.QFont()
        font.setFamily("Apple LiGothic")
        font.setPointSize(70)
        font.setBold(True)
        font.setWeight(75)

        self.titleLabel.setFont(font)
        self.titleLabel.setAutoFillBackground(False)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")

        self.gameLogFrame = QtWidgets.QFrame(main_window)
        self.gameLogFrame.setGeometry(QtCore.QRect(0, 380, 480, 180))
        self.gameLogFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gameLogFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gameLogFrame.setObjectName("gameLogFrame")

        self.gameLogTextBox = QtWidgets.QTextEdit(self.gameLogFrame)
        self.gameLogTextBox.setGeometry(QtCore.QRect(20, 20, 440, 140))
        self.gameLogTextBox.setReadOnly(True)
        self.gameLogTextBox.setObjectName("gameLogTextBox")

        self.userInputFrame = QtWidgets.QFrame(main_window)
        self.userInputFrame.setGeometry(QtCore.QRect(0, 560, 480, 80))
        self.userInputFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.userInputFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userInputFrame.setObjectName("userInputFrame")

        self.userInputTextEdit = QtWidgets.QTextEdit(self.userInputFrame)
        self.userInputTextEdit.setGeometry(QtCore.QRect(10, 10, 360, 60))

        font = QtGui.QFont()
        font.setFamily("NanumGothic")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)

        self.userInputTextEdit.setFont(font)
        self.userInputTextEdit.setObjectName("userInputTextEdit")

        self.inputButton = QtWidgets.QPushButton(self.userInputFrame)
        self.inputButton.setGeometry(QtCore.QRect(400, 0, 80, 80))
        self.inputButton.setObjectName("inputButton")
        self.inputButton.clicked.connect(self.get_user_input)

        self.gameImageFrame = QtWidgets.QFrame(main_window)
        self.gameImageFrame.setGeometry(QtCore.QRect(0, 70, 480, 310))
        self.gameImageFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gameImageFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gameImageFrame.setObjectName("gameImageFrame")

        self.hangManImage = QtWidgets.QLabel(self.gameImageFrame)
        self.hangManImage.setGeometry(QtCore.QRect(40, 20, 400, 270))
        self.hangManImage.setScaledContents(True)  # 이미지 크기에 맞게 조정
        self.hangManImage.setObjectName("hangManImage")

        self.retranslate_ui(main_window)

        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window: QMainWindow) -> None:
        """
        UI 초기화 메서드.
        이 메서드는 UI 요소들의 텍스트를 설정합니다. 주로 다국어 지원을 위해 사용됩니다.

        :param QMainWindow main_window: UI 설정을 수행할 메인 어플리케이션.
        :return:
        """
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("HangManGame", "HangManGame"))
        self.titleLabel.setText(_translate("HangManGame", "Hang Man Game"))
        self.userInputTextEdit.setPlaceholderText(
            _translate("HangManGame", "알파벳 소문자 1글자만 입력 해주세요 (종료를 원하시면 \"종료\" 라고 입력 해주세요)"))
        self.inputButton.setText(_translate("HangManGame", "제출"))

    def get_user_input(self) -> None:
        """
        사용자가 입력한 텍스트를 가져와 처리하는 메서드.
        텍스트 입력 창의 값 가져오기 -> 입력 창 비우기 -> 큐에 내용 추가 -> 입력 이벤트 설정 순으로 수행됩니다.

        :return:
        """

        # 사용자 입력값을 받고 초기화
        user_input = self.userInputTextEdit.toPlainText()
        self.clear_user_input_text_edit()

        # input 버튼을 통해서 직접적인 값 return은 지원하지 않기에, user_input_queue에 값을 넣어두고 필요한곳에서 활용
        user_input_queue.append(user_input)
        print(user_input_queue)

        # Queue에 값 추가되고, event set
        user_input_event_manager.set_event()

    def update_hangman_image(self, image_path: str) -> None:
        """
        행맨의 이미지를 업데이트하는 메서드입니다.

        :param str image_path: 업데이트할 행맨의 이미지 경로를 입력합니다.
        :return:
        """

        pixmap = QtGui.QPixmap(image_path)
        self.hangManImage.setPixmap(pixmap)

    def update_game_log_text_box(self, message: str) -> None:
        """
        게임 로그가 표시되는 텍스트 박스를 수정하는 메서드입니다

        :param message:
        :return:
        """

        # self.clear_game_log_text_box()
        # self.gameLogTextBox.setText(message)
        cursor = self.gameLogTextBox.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(message + "\n")
        self.scrollDown()

    def scrollDown(self):
        """
        텍스트 박스를 맨 밑으로 스크롤 다운하는 메서드

        :return:
        """
        scrollbar = self.gameLogTextBox.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    def clear_game_log_text_box(self) -> None:
        """
        게임 로그를 초기화하는 메서드 (니즈에 따라, 삭제가 아닌 빈칸 추가로 기존 데이터를 남기는 방향으로 고려될 수 있음)

        :return:
        """
        self.gameLogTextBox.clear()

    def clear_user_input_text_edit(self) -> None:
        """
        사용자 입력 텍스트 박스를 초기화하는 메서드

        :return:
        """
        self.userInputTextEdit.clear()
