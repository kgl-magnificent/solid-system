#Моя зверушка
class Critter(object):
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    def __pass_time(self): #закрытый метод использутся только во время вызова других методов
        self.hunger += 1
        self.boredom += 1
    @property
    def mood(self):
        unhappiness = self.boredom + self.hunger
        if unhappiness < 5:
            m = "good"
        if 5 <= unhappiness <= 10:
            m = "not bad"
        else:
            m = "awful"
        return m
    def talk(self):
        print("Меня зовут", self.name, "и сейчас я чувствую себя", self.mood)
    def eat(self, food = 4):
        print("Thanks")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
    def __str__(self):
        rep = "Объект класса Critter\n"
        rep += "имя: " + self.name
        return rep
    def about(self):
        print(Critter)
        print(self.name)
def main():
    crit_name = input("ВВедите название зверушки")
    crit = Critter(crit_name)
    choice = None
    while choice != "0":
        print \
            ("""
            Critter Caretaker

            0 - Quit
            1 - Listen to your critter
            2 - Feed your critter
            3 - Play with your critter
            """)

        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            crit.talk()

        # feed your critter
        elif choice == "2":
            crit.eat()

        # play with your critter
        elif choice == "3":
            crit.play()
        elif choice == "about":
            crit.about()
            print(crit)

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()




