# todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.

# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.


def caesar_decode(s, step):
    result = ""
    for ch in s:
        if ch.isalpha() and "a" <= ch <= "z":
            ch = chr((ord(ch) - 97 - step) % 26 + 97)
        result += ch
    return result


input_string = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
print(caesar_decode(input_string, 6))
