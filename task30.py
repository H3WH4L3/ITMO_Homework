# todo: Вы работаете с данными цен товаров, которые приходят в разном формате.
# Создайте список числовых значений цен,  игнорируя некорректные записи.
# Все цены переведите в рубли. Задачу следует решить с использованием списковых включений.

prices = ["₽1500", "20.50 USD", "invalid", "€25.00", "$15.99", "18.99", "N/A", "¥5000"]

rates = {"USD": 80.98, "$": 80.98, "€": 94.58, "¥": 0.53, "₽": 1}

result = [
    float("".join([ch for ch in price if ch.isdigit() or ch == "."])) * rate
    for price in prices
    for sym, rate in rates.items()
    if sym in price
]
print(*[f"{value} рублей" for value in result], sep="\n")
