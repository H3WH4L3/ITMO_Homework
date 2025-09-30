# todo: Преобразуйте переменную age и foo в число
age = "23"
age = int(age)
print(f"age : {age} ({type(age)})")

# Python не даст перевести строку с буквенными значениями в число,
# поэтому сперва необходимо избавить от лишнего:
foo = "23abc"
foo_digit = int(foo[:2])
foo_string = foo[2:]
print(f"foo_digit : {foo_digit} ({type(foo_digit)})")
print(f"foo_string : {foo_string} ({type(foo_string)})")

# Преобразуйте переменную age в Boolean
age = "123abc"
age = bool(age)
print(f"age : {age} ({type(age)})")

# Преобразуйте переменную flag в Boolean
flag = 1
flag = bool(flag)
print(f"flag : {flag} ({type(flag)})")

# Преобразуйте значение в Boolean
str_one = "Privet"
str_two = ""
str_one = bool(str_one)
str_two = bool(str_two)
print(f"str_one : {str_one} ({type(str_one)})")
print(f"str_two : {str_two} ({type(str_two)})")

# Преобразуйте значение 0 и 1 в Boolean
digit_0 = bool(0)
digit_1 = bool(1)
print(f"digit_0 : {digit_0} ({type(digit_0)})")
print(f"digit_1 : {digit_1} ({type(digit_1)})")

# Преобразуйте False в строку
string_False = str(False)
print(f"string_False : {string_False} ({type(string_False)})")
