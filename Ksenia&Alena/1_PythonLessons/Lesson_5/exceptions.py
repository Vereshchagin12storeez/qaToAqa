

a = 5
# b = 1
b = 0


try:
    print(a / b)
except ZeroDivisionError:
    print("Ошибка zero devision error было отловлена")
else:
    print("Выполняется только если не было исключения")
finally:
    print("Выполняется в любом случае")




