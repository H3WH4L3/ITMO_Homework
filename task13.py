# В восточном календаре принят 60-летний цикл, состоящий из 12- летних подциклов,
# обозначаемых названиями цвета: зеленый, красный, желтый, белый и черный.
# В каждом подцикле годы носят названия животных: крысы, коровы, тигра, зайца, дракона,
# змеи, лошади, овцы, обезьяны, курицы, собаки и свиньи. По номеру года вывести его название,
# если 1984 год был началом цикла — годом зеленой крысы.

year = int(input())

colors = {
    1 : "зеленый", 
    2 : "красный", 
    3 : "желтый", 
    4 : "белый", 
    5 : "черный"
    }
animals = {
    1 : "крыса", 
    2 : "корова", 
    3 : "тигр", 
    4 : "заяц", 
    5 : "дракон", 
    6 : "змея",
    7 : "лошадь", 
    8 : "овца", 
    9 : "обезьяна", 
    10 : "курица", 
    11 : "собака", 
    12 : "свинья"
}



def china_year():
    current_color, current_animal, current_year = 1, 1, 1984
    while current_year != year:
        for _ in range(5):
            if current_color > 5:
                current_color = 1
            if current_year == year:
                break
            for _ in range(2):
                current_animal += 1
                current_year += 1
                if current_animal > 12:
                    current_animal = 1
                if current_year == year:
                    return (current_animal, current_color)
            current_color += 1


a, c = china_year()
print(animals[a], colors[c])
