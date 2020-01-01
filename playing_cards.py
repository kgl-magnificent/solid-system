#Карты
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

class Hand(object):
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "  "
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []
    def add(self, card):
        self.cards.append(card)
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)
#основная часть
def main():
    card1 = Card(rank= "A", suit= "c")
    card2 = Card(rank= "2", suit= "c")
    card3 = Card(rank= "3", suit="c")
    card4 = Card(rank= "4", suit="c")
    card5 = Card(rank= "5", suit="c")
    print(card1)#печать объекта с помощью метода __str__
    my_hand = Hand()
    print("У меня на руках сейчас: ")
    print(my_hand) #печатаются сведения об объекте с помощью метода __str__
    my_hand.add(card1)
    my_hand.add(card2)
    my_hand.add(card3)
    my_hand.add(card4)
    my_hand.add(card5)
    print("Печатаю 5 карт, которые сейчас на руках: ")
    print(my_hand)
    your_hand = Hand()
    my_hand.give(card1, your_hand)
    my_hand.give(card2, your_hand)
    print(my_hand)
    print(your_hand)
    my_hand.clear()
    print(my_hand)
    input("bb")
main()

