# Редкое слово
# Напишите программу, которая принимает на вход строку из слов через пробел, и выводит слово, которое встречается во фразе реже всего.
# Если редких слов несколько, нужно вывести то, которое меньше в лексикографическом порядке.
# Регистр слов не учитывается.

strng = input("Введите строку: ")
lst = strng.split(" ")
print(lst)

dct = {}
for word in lst:
    if dct.get(word) is None:
        dct[word] = 1
    else:
        dct[word] = dct.get(word) + 1
print(dct)

