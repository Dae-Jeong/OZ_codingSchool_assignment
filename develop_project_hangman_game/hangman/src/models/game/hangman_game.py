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
    def __init__(self):
        # 마음같아서는 Stage라는 객체 따로 만들어주고싶다.... 시간 남으면 해야지....
        self.stage = None
        self.life = None
        self.word = None
        self.user_answer = None
        self.user_answer_list = None

        self.__reset_data()

    def print(self, message: str, sep=' ', end='\n', file=None):
        print(message, sep=sep, end=end, file=file)
        game_message_queue.append(message)

    def __set_user_answer(self, new_user_answer: str) -> None:
        self.user_answer = new_user_answer

    # 데이터 초기화 로직 (게임 오버 되거나, 클리어 후 실행)
    def __reset_data(self) -> None:
        self.print("상태를 초기화합니다.")
        self.stage = 1
        self.life = MAX_LIFE
        self.word = None
        self.user_answer = ""
        self.user_answer_list = []

    # 스테이지 시작 로직
    def __stage_start(self) -> None:
        # words에 있는 단어를 랜덤으로 하나 뽑아서 다음 스테이지의 단어로 활용
        self.print(f"\n\n========== Stage{self.stage}==========")
        self.print(f"Stage{self.stage}. 새로운 스테이지가 시작되어 단어가 생성되었습니다.\n단어를 맞춰보세요!!")

        self.word = WORDS.pop(random.randint(0, len(WORDS)-1))

        # 사용자의 정답지 생성
        self.__init_user_answer()

    # 스테이지 클리어 했을 떄 로직 (추가 로직 필요하면 여기에 작성)
    def __stage_clear(self) -> None:
        # 사용자에게 클리어 보상 제공
        self.__get_stage_clear_benefit()

        # 다음 스테이지
        self.stage += 1

    # 스테이지 클리어 했을 때, 보상
    def __get_stage_clear_benefit(self) -> None:
        if self.life == MAX_LIFE:
            self.print("이미 Life가 만땅이시니 스테이지 클리어 보상으로 저의 사랑을 충전해 드리겠습니다.")
            self.__print_life()
        else:
            self.__increase_life()
            self.print("스테이지 클리어 보상으로 ", end=" ")

    # 완전히 게임 클리어
    def __game_clear(self) -> None:
        self.print("\n\n=+=+=+=+= Game Clear!! =+=+=+=+=")
        self.print(f"모든 문제를 클리어하셨습니다! 남은 생명 : {self.life}")
        self.print("다음번엔 더 많은 생명을 남길 수 있도록 노력해보세요!")
        self.print(" - FIN -  CopyRight. Bbong Company")
        self.print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=\n\n")
        self.__quit_game()

    # 완전히 게임 오버
    def __game_over(self) -> None:
        self.print(f"게임을 클리어하지 못했습니다... 정답은 {self.word} 이었습니다..!")
        self.__quit_game()

    # 게임 종료
    def __quit_game(self) -> None:
        self.print("게임이 종료되었습니다.")
        self.__reset_data()

    # 마지막 스테이지인지 체크합니다.    
    def __is_last_stage(self) -> None:
        return len(WORDS) == 0

    # 정답인지 체크합니다.
    def __is_stage_clear(self) -> bool:
        return self.word == self.user_answer

    # 살았는지 체크합니다.
    def __is_alive(self) -> bool:
        return self.life > 0
    
    # 사용자가 입력한 단어가 정답에 포함되어있는지 확인합니다.
    def __check_user_input(self, user_input: str) -> bool:
        return user_input in self.word

    # 숨겨진 정답을 열게됩니다.
    def __open_word(self, user_input: str) -> None:
        def get_covered_index_list(user_input: str) -> list[int]:
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

    # 사용자의 응답을 얻습니다.
    def __get_user_input(self) -> str:
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
        user_answer_for_print = " ".join(self.user_answer) 
        self.print(f"\n현재 사용자의 정답 현황 : {user_answer_for_print}")

    def __validate_user_input(self, user_input: str) -> bool:
        # 길이가 1글자가 아닌 경우 (나중에 로직 많아지면 별도 메서드로 분리)
        if len(user_input) != 1:
            self.print("소문자 알파벳 1글자만 입력해 주세요")
            return False
        
        # 단어가 소문자 알파벳이 아닌 경우
        if user_input not in ALPHABET:
            self.print("소문자 알파벳 1글자만 입력해 주세요")
            return False
        
        if user_input in self.user_answer_list:
            self.print("이미 입력하셨던 응답입니다. 다시한번 생각해보세요")
            return False
        
        return True

    def __reduce_life(self, x: int = 1) -> None:
        self.life -= x
        self.print(f"Life가 {x}만큼 감소했습니다.")
        self.__print_life()

    def __increase_life(self, x: int = 1) -> None:
        self.life += x
        self.print(f"Life가 {x}만큼 추가 되었습니다")
        self.__print_life()

    def __print_life(self) -> None:
        self.print(f"현재 Life : [{self.life}/{MAX_LIFE}]")
        self.display()

    # 사용자의 정답지를 생성 및 중복 방지용 리스트를 초기화합니다
    def __init_user_answer(self) -> None:
        self.__set_user_answer("_" * len(self.word))
        self.user_answer_list.clear()

    def display(self) -> None:
        hangman_pic = HANGMAN_IMG_DICT.get(self.life)
        hangman_image_queue.append(hangman_pic)

    def play(self) -> None:
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
