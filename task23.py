# todo: Исправить ошибку в коде игры  ../code/ya_kube.py

import random
import uuid
import datetime
from db import DICT_DEFENITION_WORD

name = input("Введите имя:")

def print_menu():
    print("""   
       1. Начать игру
       2. Сохранить игру
       3. Загрузить игру
       4. Выход из игры
       5. Настройки 
    """)

print_menu()
num = int(input("Пункт меню:"))

def generate_key() -> str:
    keys = list(DICT_DEFENITION_WORD.keys())
    random.shuffle(keys)
    return keys.pop()

def save_game(id_session, word, mask):
    # dt, id_session, name, word, mask
    f = open("save_game.csv", "at", encoding="utf-8")
    dt = datetime.datetime.now()
    mask_str = "".join(mask)
    line = f"{dt}|{id_session}|{name}|{word}|{mask_str}\n"
    f.write(line)
    f.close()
    print("Сохранил игру!")

def load_game():
    f = open("save_game.csv", "tr", encoding="utf-8")
    indx = 0
    list_str = f.readlines()
    f.close()
    for csv_str in list_str:
        if name in csv_str:
            print(indx, ") ", csv_str, end="")
        indx += 1
    indx_load = int(input("Введите номер:"))
    sg = list_str[indx_load].split("|")
    key = sg[3].strip()
    mask = sg[4].strip()  # было с \n в конце
    session_uuid = sg[1]
    print(session_uuid, key, list(mask))
    start_game(session_uuid, key, list(mask))
    exit(0)

def start_game(session_uuid, key, mask):

    print(DICT_DEFENITION_WORD[key])
    print(mask)
    list_word = list(key)
    while '#' in mask:
        alfa = input("Введите букву:")
        if alfa == "2":
            print("Сохранение игры!")
            save_game(session_uuid, key, mask)
            continue
        cnt = 0
        for i in list_word:
            if alfa == i:
                mask[cnt] = alfa
            cnt += 1
        else:
            print(mask)

match num:
    case 1:
        key = generate_key()
        mask = ['#'] * len(key)
        session_uuid = uuid.uuid4()
        start_game(session_uuid, key, mask)
    case 2:
        pass
    case 3:
        load_game()
    case 4:
        print(f"Спасибо {name} за игру! Заходи еще! ")
        pass
