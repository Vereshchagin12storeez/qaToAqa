# Написать программу симулятор кассира в магазине. К кассиру ПОСТОЯННО приходят люди в надежде купить пиво или спички.
# Необходимо проверять возраст покупателя и выводить результат проверки. При вводе пробела - рабочий день кончается.

# Со звёздочкой: Добавить список имеющихся продуктов в магазине и проверять имеются ли они

products = ["пиво", "спички", "хлеб", "молоко"]

while True:
    product = input("Введите название продукта: ")

    if product == "":
        print("Рабочий день окончен")
        break
    if product not in products:
        print("Такого продукта нет в магазине ")
    elif product == "пиво" or product == "спички":
        age = input("Введите возраст покупателя: ")
        if int(age) < 18:
            print("Покупатель не может купить")
        elif int(age) >= 18:
            print("Покупатель может купить")
        else:
            print("Неверно введен возраст")

    else:
        print("Покупатель может купить. Товар есть в магазине")





