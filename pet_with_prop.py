#зверушка со свойствами
#свойства допускают чтение из атрибута, но запрещают его изменение
class Critter(object):
    def __init__(self, name):
        print("Появилась на свет новая звершука")
        self.__name = name
#для создания свойства необходимо создать метод, который возвращает интересующее нас значение
    @property
    def name(self):
        return self.__name
#делаем возможным для записи закрытый атрибут __name
    @name.setter # name - имя свойства setter - имя
    def name(self, new_name):
        if new_name == "":
            print("Имя не может быть пустым")
        else:
            self.__name = new_name
            print("Имя успешно изменено")
    def talk(self):
        print("\nПривет, меня зовут", self.name)
#Основная часть
crit = Critter("Бобик")
crit.talk()

print("Мою зверушку зовут:")
print(crit.name)

#меняю имя на Мурзик
crit.name = "Мурзик"

print(crit.name)

crit.name = ""
print(crit.name)

