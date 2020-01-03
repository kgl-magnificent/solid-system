#Карты 3.0
class Card(object):
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"] #атрибут класса Cards
    SUITS = ["c", "d", "h", "s"]
    def __init__(self, rank, suit):
        self.rank = rank #устанавливаем значение карты
        self.suit = suit #устанавливаем масть карты
    def __str__(self):
        rep = self.rank + self.suit #2 атрибута образуют карту
        return rep
class Unpredictable_Card(Card):
    def __str__(self): #переопределение метода __str__()
        return "<нельзя напечатать>"

class Positionable_Card(Card):
    def __init__(self, rank, suit, face_up = True):
        super(Positionable_Card, self).__init__(rank, suit)#функц. super() вызывает метод базового класса Card
        self.is_face_up = face_up
    def __str__(self):
        if self.is_face_up:
            rep = super(Positionable_Card, self).__str__()
        else:
            rep = "XX"
        return rep
    def flip(self):
        self.is_face_up = not self.is_face_up
#основная часть
card1 = Card("A", "c") #параметры задаются через __init__()
card2 = Unpredictable_Card("A", "d")
card3 = Positionable_Card("A", "h")
print(card1)
print(card2)#используется переопределенные методы базового класса Card()
print(card3)
card3.flip()#карту перевернули
print(card3)
