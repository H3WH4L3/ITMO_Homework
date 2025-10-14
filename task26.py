# todo:  Задан файл dump.txt. Необходимо для заданного файла подсчитать статистику количества
# гласных букв в тексте.

# Формат вывода:
# - Количество букв a - 13
# - Количество букв o - 12
# - Количество букв e - 11
# - .....................

# После pull не не удалось найти файл dump.txt, поэтому создал временно свой. Скрипт должен работать на любых вводных, удовлетворяющих основным условиям!

vowels_count = {
    "а": 0,
    "о": 0,
    "у": 0,
    "ы": 0,
    "э": 0,
    "е": 0,
    "ё": 0,
    "и": 0,
    "ю": 0,
    "я": 0,
}

with open("dump.txt", "r", encoding="UTF-8") as f:
    data = f.read()

for ch in data:
    if ch.isalpha() and ch.lower() in vowels_count:
        vowels_count[ch] = vowels_count.get(ch) + 1

for key, value in vowels_count.items():
    if not value:
        continue
    print(f"- Количество букв {key} - {value}")
