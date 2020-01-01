#Гибель пришельца
#Деманстрирует взаимодействие объектов
class Player(object):
    #Игрок
    def blaster(self, enemy):#этот метод принимает аргумент в параметр enemy, поэтому используется invader
        enemy.die() #вызывается метод die класса Alien

class Alien(object):
    #Инопланетянин
    def die(self):
        print("Я умер")

def main():
    print("Гибель пришелшьца")
    hero = Player()
    invader = Alien()
    hero.blaster(invader) #аргумент необязательно называть enemy; вызывется метод blaster объекта hero
    #и передается как аргумент объукт invader
main()



