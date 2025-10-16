# todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.

# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.


# 97 122
def caesar_decode(s, step):
    out = ""
    for ch in s:
        if "a" <= ch <= "z":
            ch = chr((ord(ch) - 97 - step) % 26 + 97)
        out += ch
    return "".join(out)


input_string = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
print(caesar_decode(input_string, 6))
