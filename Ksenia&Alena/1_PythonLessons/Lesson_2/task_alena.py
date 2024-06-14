# Редкое слово
# Напишите программу, которая принимает на вход строку из слов через пробел, и выводит слово,
# которое встречается во фразе реже всего.
# Если редких слов несколько, нужно вывести то, которое меньше в лексикографическом порядке.
# Регистр слов не учитывается.

def words_counter(lst):
    dct = {}
    for wrd in lst:
        if not dct.get(word):
            dct[word] = 1
        else:
            dct[word] += 1
    return dct


# "word bike flower word qweq word flower bike qweq bike"
words_string = input("Введите строку: ")
words_lst = words_string.split(" ")

words_dict = words_counter(words_lst)

print(words_dict)

min_count_word = []
min_counter = 0

for word, counter in words_dict.items():
    if counter <= min_counter:
        min_counter = counter
        min_count_word.append(word)

print(min_count_word)
