class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(f"{self.name} гуляет.")

    def sleep(self):
        print(f"{self.name} спит.")


class Salesman(Human):
    def __init__(self, name, age, products_list):
        super().__init__(name, age)
        self.products_list = products_list

    def get_salesman_name(self):
        print(self.name)

    def sale(self, product):
        if product in self.products_list:
            return "Покупка удалась"
        else:
            return "Товара нет у продавца"


sasha_saleman = Salesman(name="Sasha",
                         age=12,
                         products_list=["молоко", "хлеб"])

sasha_saleman.sleep()
sasha_saleman.walk()
sasha_saleman.get_salesman_name()
