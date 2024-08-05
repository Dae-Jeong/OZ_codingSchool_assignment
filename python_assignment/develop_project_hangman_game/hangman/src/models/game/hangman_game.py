from src.utils import (singleton,
                       user_input_event_manager, user_input_queue,
                       game_message_queue,
                       hangman_image_queue)

import random
import string

MAX_LIFE = 10
ALPHABET = {alphabet: None for alphabet in string.ascii_lowercase}

# 게임에 사용될 단어 목록
WORDS = ["apple", "banana", "orange", "grape", "lemon"]

# display에 활용될 hangman pics
__base_image_path = 'resources/imgs/hangman_{}.jpg'
HANGMAN_IMG_DICT = {i: __base_image_path.format(10 - i) for i in range(11)}
HANGMAN_BASE_IMG = HANGMAN_IMG_DICT.get(10)
""" Result

HANGMAN_IMG_DICT = {
    0: 'resources/imgs/hangman_10',
    1: 'resources/imgs/hangman_9',
    ...
    9: 'resources/imgs/hangman_1',
    10: 'resources/imgs/hangman_0',
}
"""


@singleton
class HangmanGame:
    """
    Hangman 게임을 관리하는 클래스입니다.

    Attributes:
        stage (optional[None, int]): 현재 게임 스테이지
        life (optional[None, int]): 현재 생명
        word (optional[None, str]): 현재 문제 단어
        user_answer (optional[None, str]): 사용자의 정답 시도
        user_answer_list (optional[None, list[str]]): 사용자가 이미 시도한 답안들의 리스트
    """
    def __init__(self):
        """
        HangmanGame 객체의 초기화 메서드입니다.
        """
        self.stage = None
        self.life = None
        self.word = None
        self.user_answer = None
        self.user_answer_list = None

        self.__reset_data()

    def print(self, message: str, sep=' ', end='\n', file=None) -> None:
        """
        메시지를 출력하고, 출력된 메시지를 game_message_queue에 추가하는 메서드입니다.

        :param str message: 출력할 메시지
        :param str sep: 출력할 메시지 사이의 구분 문자. 기본값은 공백입니다.
        :param str end: 출력의 마지막에 추가할 문자열. 기본값은 개행입니다.
        :param file: 출력할 파일 객체. 기본값은 None입니다.
        """
        print(message, sep=sep, end=end, file=file)
        game_message_queue.append(message)

    def __set_user_answer(self, new_user_answer: str) -> None:
        """
        사용자의 정답 시도를 설정하는 메서드입니다.

        :param str new_user_answer: 새로운 사용자 정답 시도
        """

        self.user_answer = new_user_answer

    def __reset_data(self) -> None:
        """
        게임 데이터를 초기화하는 메서드입니다.
        """

        self.print("상태를 초기화합니다.")
        self.stage = 1
        self.life = MAX_LIFE
        self.word = None
        self.user_answer = ""
        self.user_answer_list = []

    def __stage_start(self) -> None:
        """
        새로운 스테이지를 시작하는 메서드입니다.
        """

        self.print(f"\n\n========== Stage{self.stage}==========")
        self.print(f"Stage{self.stage}. 새로운 스테이지가 시작되어 단어가 생성되었습니다.\n단어를 맞춰보세요!!")

        self.word = WORDS.pop(random.randint(0, len(WORDS)-1))

        # 사용자의 정답지 생성
        self.__init_user_answer()

    def __stage_clear(self) -> None:
        """
        스테이지를 클리어했을 때의 처리를 수행하는 메서드입니다.
        """

        self.__get_stage_clear_benefit()
        self.stage += 1

    def __get_stage_clear_benefit(self) -> None:
        """
        스테이지 클리어 보상을 제공하는 메서드입니다.
        """

        if self.life == MAX_LIFE:
            self.print("이미 Life가 만땅이시니 스테이지 클리어 보상으로 저의 사랑을 충전해 드리겠습니다.")
            self.__print_life()
        else:
            self.__increase_life()
            self.print("스테이지 클리어 보상으로 ", end=" ")

    def __game_clear(self) -> None:
        """
        게임을 완전히 클리어했을 때의 처리를 수행하는 메서드입니다.
        """

        self.print("\n\n=+=+=+=+= Game Clear!! =+=+=+=+=")
        self.print(f"모든 문제를 클리어하셨습니다! 남은 생명 : {self.life}")
        self.print("다음번엔 더 많은 생명을 남길 수 있도록 노력해보세요!")
        self.print(" - FIN -  CopyRight. Bbong Company")
        self.print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=\n\n")
        self.__quit_game()

    def __game_over(self) -> None:
        """
        게임이 종료되었을 때의 처리를 수행하는 메서드입니다.
        """

        self.print(f"게임을 클리어하지 못했습니다... 정답은 {self.word} 이었습니다..!")
        self.__quit_game()

    def __quit_game(self) -> None:
        """
        게임을 종료하는 메서드입니다.
        """

        self.print("게임이 종료되었습니다.")
        self.__reset_data()

    def __is_last_stage(self) -> None:
        """
        마지막 스테이지인지 확인하는 메서드입니다.

        :return: 마지막 스테이지이면 True, 아니면 False
        :rtype: bool
        """

        return len(WORDS) == 0

    def __is_stage_clear(self) -> bool:
        """
        현재 스테이지가 클리어되었는지 확인하는 메서드입니다.

        :return: 스테이지가 클리어되었으면 True, 아니면 False
        :rtype: bool
        """

        return self.word == self.user_answer

    def __is_alive(self) -> bool:
        """
        사용자가 생존해 있는지 확인하는 메서드입니다.

        :return: 생존하고 있으면 True, 아니면 False
        :rtype: bool
        """

        return self.life > 0
    
    def __check_user_input(self, user_input: str) -> bool:
        """
        사용자 입력이 정답에 포함되어 있는지 확인하는 메서드입니다.

        :param str user_input: 사용자 입력 문자열

        :return: 정답에 포함되어 있으면 True, 아니면 False
        :rtype: bool
        """

        return user_input in self.word

    def __open_word(self, user_input: str) -> None:
        """
        사용자의 정답이 정답 단어에 포함되어 있을 경우, 정답을 공개하는 메서드입니다.

        :param str user_input: 사용자 입력 문자열
        """

        def get_covered_index_list(user_input: str) -> list[int]:
            """
            사용자 입력 문자가 정답 단어에서 어떤 인덱스에 위치해 있는지 반환하는 메서드입니다.

            :param str user_input: 사용자 입력 문자열

            :return: 정답 단어에서 사용자 입력 문자가 위치한 인덱스 리스트
            :rtype: list[int]
            """

            covered_index_list = []

            for idx, char in enumerate(self.word):
                if char == user_input:
                    covered_index_list.append(idx)

            return covered_index_list

        covered_index_list = get_covered_index_list(user_input=user_input)

        user_answer_char_list = list(self.user_answer)
        for idx in covered_index_list:
            user_answer_char_list[idx] = user_input

        self.__set_user_answer(new_user_answer="".join(user_answer_char_list))

    def __get_user_input(self) -> str:
        """
        사용자 입력을 받는 메서드입니다.

        :return: 사용자 입력 문자열
        :rtype: str
        """

        while True:
            # user_input = input("원하는 소문자 알파벳을 1글자만 입력하세요 (종료를 원한다면 '종료'를 입력하세요) : ")

            self.print("원하는 소문자 알파벳을 1글자만 입력하세요\n(종료를 원한다면 '종료'를 입력하세요)")
            user_input_event_manager.wait_for_event()
            user_input = user_input_queue.pop()
            user_input_event_manager.clear_event()

            if user_input == "종료":
                return user_input

            if self.__validate_user_input(user_input=user_input):
                # 정답 중복 입력 방지를 위해 입력 리스트에 추가
                self.user_answer_list.append(user_input)
                return user_input
        
    def __print_user_answer(self) -> None:
        """
        현재 사용자의 정답 상태를 출력하는 메서드입니다.
        """

        user_answer_for_print = " ".join(self.user_answer) 
        self.print(f"\n현재 사용자의 정답 현황 : {user_answer_for_print}")

    def __validate_user_input(self, user_input: str) -> bool:
        """
        사용자 입력이 유효한지 검사하는 메서드입니다.
        조건1. 단어가 1글자 이상인 경우
        조건2. 단어가 소문자 알파벳이 아닌 경우
        조건3. 이미 사용자가 입력했던 단어인 경우

        :param str user_input: 사용자 입력 문자열

        :return: 사용자 입력이 유효하면 True, 아니면 False
        :rtype: bool
        """

        if len(user_input) != 1:
            self.print("소문자 알파벳 1글자만 입력해 주세요")
            return False
        
        if user_input not in ALPHABET:
            self.print("소문자 알파벳 1글자만 입력해 주세요")
            return False
        
        if user_input in self.user_answer_list:
            self.print("이미 입력하셨던 응답입니다. 다시한번 생각해보세요")
            return False
        
        return True

    def __reduce_life(self, x: int = 1) -> None:
        """
        생명을 감소시키는 메서드입니다.
        """

        self.life -= x
        self.print(f"Life가 {x}만큼 감소했습니다.")
        self.__print_life()

    def __increase_life(self, x: int = 1) -> None:
        """
        생명을 증가시키는 메서드입니다.
        """

        self.life += x
        self.print(f"Life가 {x}만큼 추가 되었습니다")
        self.__print_life()

    def __print_life(self) -> None:
        """
        현재 생명 상태를 출력하는 메서드입니다.
        """

        self.print(f"현재 Life : [{self.life}/{MAX_LIFE}]")
        self.display()

    def __init_user_answer(self) -> None:
        """
        사용자의 정답 시도를 초기화하는 메서드 입니다.
        초기화된 문자열의 길이는 해당 스테이지의 정답 단어 길이와 같습ㄴ니다.
        """
        self.__set_user_answer("_" * len(self.word))
        self.user_answer_list.clear()

    def display(self) -> None:
        """
        현재 생명 상태를 기준으로 행맨 이미지 경로를 받아옵니다.
        받아온 이미지 경로를 hangman_image_queue에 추가하는 메서드 입니다.
        """

        hangman_pic = HANGMAN_IMG_DICT.get(self.life)
        hangman_image_queue.append(hangman_pic)

    def play(self) -> None:
        """
        Hangman 게임을 실행하는 메서드입니다.
        """

        # 지금이 마지막 스테이지가 아니라면 (스테이지 반복문)
        while not self.__is_last_stage():
            # 스테이지 시작
            self.__stage_start()
    
            # 반복해서 정답 여부 확인
            while not self.__is_stage_clear():
                self.__print_user_answer()
                # 사용자의 입력 데이터 제공
                user_input = self.__get_user_input()

                # 사용자가 중간에 종료를 입력했다면, 게임 종료
                if user_input == "종료":
                    self.__quit_game()
                    return

                # 정답인지 확인
                if self.__check_user_input(user_input=user_input):
                    # 정답일 경우 사용자 정답지에 단어 공개
                    self.__open_word(user_input=user_input)
                    self.print("단어를 맞추셨군요. 더 힘내봐요")
                else:
                    # 오답이라면 생명이 깎임
                    self.__reduce_life()

                    # 게임 지속 가능한지 확인
                    if self.__is_alive():
                        self.print(f"틀렸습니다. 남은 시도 횟수 : {self.life}")
                    else:
                        # 지속이 불가능하다면 게임 오버
                        self.__game_over()
                        return

            # 정답일 경우 스테이지 클리어 판정 후 다음 스테이지
            self.__stage_clear()

        # 더 이상 지속할 단어가 없을 경우 게임 클리어
        self.__game_clear()
