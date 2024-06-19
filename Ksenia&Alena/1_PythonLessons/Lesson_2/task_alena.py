# Редкое слово
# Напишите программу, которая принимает на вход строку из слов через пробел, и выводит слово, которое встречается во фразе реже всего.
# Если редких слов несколько, нужно вывести то, которое меньше в лексикографическом порядке.
# Регистр слов не учитывается.

# bus ron fen bus fen ron bus
lst = input("Введите строку: ").split(" ")

dct = {}
for word in lst:
    if dct.get(word) is None:
        dct[word] = 1
    else:
        dct[word] += 1


min_quantity = dct[word]
min_word = word
for word, quantity in dct.items():
    if dct[word] < min_quantity:
        min_quantity = dct[word]
        min_word = word
    elif dct[word] == min_quantity and word < min_word:
        min_word = word

print(f"{min_word}: {min_quantity}")
