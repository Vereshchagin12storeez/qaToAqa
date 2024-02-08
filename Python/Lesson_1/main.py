

def salesman(number):
    if number > 18:
        return "Продать пиво"
    elif number >= 16:
        return "Продать спички"
    else:
        return 'Пошёл вон!!!'

num = int(input("Введите ваш возраст: "))
answer = salesman(num)

print(answer)

