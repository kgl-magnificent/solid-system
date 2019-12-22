#Зверушка с атрибутом
#Демонстрирует создание атрибутов объекта и доступа к ним
class Critter(object):
    def __init__(self, name): #первый параметр становится ссылкой на объект, по отношению к
        #к которому он вызван
        print("Появилась на свет новая тварь)")
        self.name = name
    def __str__(self): #метод применяется для представления объекта строками
        rep = "Объект класса Critter\n"
        rep += "имя: " + self.name + "\n"
        return rep

    def talk(self):  # обьявление метода
        print("Привет, я новый обьект класса Critter.py")
        #
#основная часть
crit1 = Critter("Бобик")
crit1.talk()
crit2 = Critter("Мурзик")
crit2.talk()
print("Вывод объекта crit1 на экран: ")
print(crit1)
print(crit1.name)
input("1")
