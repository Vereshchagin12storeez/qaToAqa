# Необходимо написать программу которая проходит по списку абитуриентов, они вводят свои оценки по предметам.
# После чего программа сообщает поступил абитуриент или нет.

# Со звёздочкой: добавить ограничение количества мест в университете.

applicant_names = ["Петя", "Света", "Вася", "Алина", "Никита"]
success_number = 230
places = 2

for i in applicant_names:
    if places <= 0:
        print("Мест больше нет!")
        break
    print(i)
    russian_mark = int(input("Введите количество баллов по русскому языку: "))
    math_mark = int(input("Введите количество баллов по математике: "))
    chemistry_mark = int(input("Введите количество баллов по химии: "))
    summ = russian_mark + math_mark + chemistry_mark
    if summ >= success_number:
        print(f"{i} поступил")
        places -= 1
    else:
        print(f"{i} не поступил")