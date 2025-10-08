# todo: База данных пользователя.
# Задан массив объектов пользователя

# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.

#Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе

# тип сортировки: 1

#Затем сообщение для ввода
# Ввидите критерии поиска: 16

# Результат:
# Пользователь: 'Piter' возраст 23 года , группа  "admin"
# Пользователь: 'Dasha' возраст 30 лет , группа  "master"

users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

def year_word(n):
    if 5 <= (n % 100) <= 20:
        return "лет"
    last = n % 10
    if last == 1:
        return "год"
    if 2 <= last <= 4:
        return "года"
    return "лет"

def sort_key(element):
    key = sort_rule
    match key:
        case 1:
            return element["age"] > int(sort_value)
        case 2:
            return element["login"][0] == sort_value
        case 3:
            return element["group"] == sort_value

sorte_rules = {
    1 : "age",
    2 : "login"[0],
    3 : "group"
}

sort_rule = int(input("""
                      Укажите тип сортировки:
                      \n1. По возрасту
                      \n2. По первой букве
                      \n3. По группе
                      \n> """))
sort_value = input("Укажите критерий поиска:\n> ")

result = list(filter(sort_key, users))

if sort_rule == 1:
    result = sorted(result, key=lambda u: u["age"])
elif sort_rule == 2:
    result = sorted(result, key=lambda u: u["login"].lower())
elif sort_rule == 3:
    result = sorted(result, key=lambda u: (u["group"].lower(), u["age"]))

if not result:
    print("Ничего не найдено по заданному критерию.")
else:
    for e in result:
        print(f'Пользователь: `{e["login"]}` возраст {e["age"]} {year_word(e["age"])} , группа "{e["group"]}"')