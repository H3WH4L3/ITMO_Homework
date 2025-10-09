#todo: Выведите все строки данного файла в обратном порядке, допишите их в этот же файл.
# Для этого считайте список всех строк при помощи метода readlines().

# #Содержимое файла inverted_sort.txt
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

# # Результат
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.

with open("inverted_sort.txt", mode="a+", encoding="UTF-8") as f:
    f.seek(0)
    text = f.readlines()
    
    if text and not text[-1].endswith("\n"):
        f.write("\n")

    for line in text[::-1]:
        if not line.endswith("\n"):
            line += "\n"
        f.write(line)
