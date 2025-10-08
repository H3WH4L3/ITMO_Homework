#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.
# Одинаковых значение может быть два и более !
# Пример:
# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.

mass = [1,2,17,54,30,89,2,1,6,2]

def find_distance(m, digit):
    if m.count(digit) < 2:
        return f"Для числа {digit} нет минимального расстояния. Он в массиве один"
    else:
        first, second, result  = (0, 0, len(mass))
        start = 0
        while True:
            try:
                x = m.index(digit, start)
                y = m.index(digit, x+1)
                z = y - x
                if z < result:
                    first, second, result = (x, y, z)
                start += 1
            except ValueError:
                break
        return f"Для числа {digit} минимальное расстояние в массиве по индексам: {first} и {second}"

for element in set(mass):
    print(find_distance(mass, element))