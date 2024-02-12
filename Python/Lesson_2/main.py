# class A:
#     def __init__(self, browser):
#         super().__init__(browser)


class Auto:
    def __init__(self, name='auto', year='1990'):
        self.name = name
        self.year = year

    def drive(self):
        print("Машина едет")

    def open_door(self):
        print("Открывает дверь")


class BMW(Auto):

    def crashing(self):
        print("Я бмв, я ломаюсь")
        self.name = "Сломанная бмв"

    def drive(self):
        print("БМВ едет быстро")
        self.crashing()


auto = Auto()

bmw = BMW(name='bmw', year='1990')
# bmw2 = BMW(name='bmw', year='2020')

print(bmw.name)
bmw.drive()

