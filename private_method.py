#использование закрытых атрибутов
class Critter(object):
    def __init__(self, name, mode):
        print("Появилась на свет новая зверушка!")
        self.name = name #открытый атрибут
        self.__mode = mode #закрытый атрибут для ограничения доступа
    def talk(self):
        print("\nМеня зовут", self.name)
        print("Сейчас я чувствую себя", self.__mode) #закрытый атрибут используется только внутри кл.
    def __private_method(self):
        print("Это закрытый метод")
    def public_method(self):
        print("Это открытый метод")
        self.__private_method()
#основная часть
crit = Critter(name = "Бобик", mode = "прекрасно")
crit.talk()
crit.public_method()
input("1")


