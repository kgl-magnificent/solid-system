#Простоя зверушка
#Демонстрирует простейший класс
class Critter(object): #объявление класса #заголовок класса
    """Виртуальный питомец"""
    def talk(self): #обьявление метода
        print("Привет, я новый обьект класса Critter.py")
#Основная часть
crit = Critter() #создание объекта класса
crit.talk() #вызов метода
input("\n\nНажмите Enter, чтобы выйти")