#Карты 3.0
class Card(object):
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"] #атрибут класса Cards
    SUITS = ["c", "d", "h", "s"]
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        rep = self.rank + self.suit #2 атрибута образуют карту
        return rep
class Unpredictable_Card(Card):
    def __str__(self): #переопределение метода __str__()
        return "<нельзя напечатать>"

