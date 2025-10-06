#  todo: Дан номер месяца (1 — январь, 2 — февраль, ...). Вывести название соответствующего
#  времени года ("зима", "весна" и т.д.).

test_input = int(input("Введите номер месяца: "))

#region Первый вариант
seasons = {
    0 : "зима",
    1 : "весна",
    2 : "лето",
    3 : "осень"
}
months = [
    [12, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [9, 10, 11]
]

for i in range(len(months)):
    if test_input in months[i]:
        print(seasons[i])
#endregion

#region Второй вариант
seasons_ = {
    "зима" : [12, 1, 2],
    "весна" : [3, 4, 5],
    "лето" : [6, 7, 8],
    "осень" : [9, 10, 11]
}

for key, value in seasons_.items():
    if test_input in value:
        print(key)