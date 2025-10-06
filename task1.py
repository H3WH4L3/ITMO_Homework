# todo: Определить в коде переменные:
# 1. Целочисленного типа
x = 10
# 2. Вещественного типа
y = 1.2
# 3. Логического типа
flag = True
# 4. Строкового типа
s = "Some string"
# 5. Пустого типа
empty = None
# Вывести их типы (надо погуглить)

for element in [x, y, flag, s, empty]:
    print(f'{element} type: {type(element)}')