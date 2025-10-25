# todo: Перепишите игру "Поле чудес" на классах.
from random import choice
import uuid
from datetime import datetime
import os
from db import DICT_DEFENITION_WORD


def clear():
    os.system("cls" if os.name == "nt" else "clear")


class Yakubovich:
    def __init__(self):
        self._session_uuid = None
        self._key = None
        self._mask = None
        self._name = input("Укажите Ваше имя: ")

    def print_menu(self):
        clear()
        print(
            """   
        1. Начать игру
        2. Сохранить игру
        3. Загрузить игру
        4. Выход из игры
        5. Настройки 
        """
        )
        num = int(input("Пункт меню: "))
        match num:
            case 1:
                self._key = self._generate_key()
                self._session_uuid = uuid.uuid4()
                self._mask = ["#"] * len(self._key)
                self.start_game()
            case 2:
                self.save_game()
            case 3:
                self.load_game()
            case 4:
                self.end_game()
            case 5:
                clear()
                print("Какие это тебе настройки в терминале?\n")
                input("Нажмите Enter чтобы продолжить...")
                self.print_menu()

    def start_game(self):
        while "#" in self._mask:
            clear()
            print(DICT_DEFENITION_WORD[self._key].capitalize())
            print(self._mask)
            alfa = input("Введите букву: ")
            if alfa == "2":
                self.save_game()
            elif alfa == "3":
                self.load_game()

            for i, e in enumerate(list(self._key)):
                if alfa == e:
                    self._mask[i] = alfa
        self.end_game()

    def save_game(self):
        clear()
        if not self._session_uuid:
            print("Вы еще не начали ни одной игры!\n")
            input("Нажмите Enter чтобы продолжить...")
            self.print_menu()

        # Body
        with open("save_game.csv", "at", encoding="UTF-8") as f:
            dt = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            mask = "".join(self._mask)
            save_string = f"{dt}|{self._session_uuid}|{self._name}|{self._key}|{mask}"
            f.write(save_string + "\n")
        print("Игра сохранена!\n")
        input("Нажмите Enter чтобы продолжения...")

    def end_game(self):
        clear()
        if not self._key:
            print("В следующий раз обязательно попробуй поиграть!")
            input()
            exit(0)
        print(
            f"Вы победили!\n{DICT_DEFENITION_WORD[self._key].capitalize()} - это, конечно же '{self._key.upper()}!"
        )
        input()
        self._session_uuid, self._key, self._mask = (None, None, None)
        self.print_menu()

    def load_game(self):
        clear()
        with open("save_game.csv", "tr", encoding="UTF-8") as f:
            list_str = f.readlines()
            for index, csv_str in enumerate(list_str):
                line = csv_str.split("|")
                print(
                    f"{index}.\n \tИмя: {line[2]}\n \tПрогресс: {line[4].rstrip()}\n \tВремя: {line[0]}"
                )

            index_load = int(input("Введите номер: "))
            choosen_save = list_str[index_load].split("|")
        self._session_uuid = choosen_save[1]
        self._key = choosen_save[3]
        self._mask = list(choosen_save[4].rstrip())

        self.start_game()

    def _generate_key(self) -> str:
        return choice(list(DICT_DEFENITION_WORD.keys()))


game = Yakubovich()
game.print_menu()
