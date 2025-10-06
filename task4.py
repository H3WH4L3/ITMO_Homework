# todo: Заданы три числа в переменных x, y, z.
# Напечатать наибольшее из этих чисел.
# Пример:
x = 10
y = 15
z = 2
# # Ответ:
# Наибольшее число 15

# Пример:
# x = 77
# y = 9
# z = 130
# Ответ:
# Наибольшее число 130

# Задачу решить без функций max и прочих.
# Значение переменных может меняться

# Первый вариант
max_value = x
for element in [x, y, z]:
    if element > max_value:
        max_value = element
print("Вариант 1: ", max_value)

# Второй вариант
if y > max_value:
    max_value = y
if z > max_value:
    max_value = z
print("Вариант 2: ", max_value)
