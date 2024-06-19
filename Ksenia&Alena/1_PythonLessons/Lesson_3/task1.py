"""
Дополнить функцию магазина чтобы она проверяла есть ли товар в магазине.
Если товар имеется, то функция должна возвращать купленный товар.
Если товара нет, то должно возвращаться и выводится сообщение, что товара нет в наличии.
Пользователь должен сходить в магазин 5 раз.
"""
products_in_shop = {"молоко": 5, "хлеб": 3, "вода": 4, "масло": 0}
# Для того чтобы получить value из словаря можно использовать: products_in_shop.get("молоко/другое значение")
# Для того чтобы изменить value в словаре: products_in_shop["молоко/другой ключ"] = новое значение


def shop(product, amount=1):
    if not products_in_shop.get(product): # в случае если такого ключа нет - вернётся значение None(False по сути)
        return "Товара нет в магазине"
    # Вставить свой код сюда


# product_to_buy = input("Введите товар который хотите приобрести: ").lower()
# amount_of_product = int(input("Введите желаемое количество товара: "))
#
# result = shop(product_to_buy)


def shop(product, amount):
    product_real_amount = products_in_shop.get(product)
    if not product_real_amount:  # в случае если такого ключа нет - вернётся значение None(False по сути)
        return "Товара нет в магазине"

    if product_real_amount < amount:
        return f"В магазине нет столько {product}. Осталось всего {product_real_amount}"

    products_in_shop[product] -= amount
    return "Товар приобретён"


for i in range(1, 6):
    print(f"Поход в магазин №{i}.")
    product_to_buy = input("Введите товар который хотите приобрести: ").lower()
    amount_of_product = int(input("Введите желаемое количество товара: "))

    result = shop(product_to_buy, amount_of_product)
    print(result)
