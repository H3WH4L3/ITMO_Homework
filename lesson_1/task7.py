#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().

A, B, C = map(int, input().split())

# Длина отрезка AC:
print("Длина отрезка AC: ", end="")
segment_AC = abs(A - C)
print(segment_AC)

# Длина отрезка BC:
print("Длина отрезка BC: ", end="")
segment_BC = abs(B - C)
print(segment_BC)

# Сумма отрезков
print("Сумма отрезков AC и BC: ", end="")
print(segment_AC + segment_BC)