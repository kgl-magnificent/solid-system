#Карты 2.0
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
        self.cards.append(card) #append добавление метод списка
    def give(self, card, other_hand):
        self.cards.remove(card) #remove удаление из списка
        other_hand.add(card) #метод give использует  другой метод add класса hand
class Deck(Hand):#добавляем методы в производном классе Deck к базовому классу Hand
    def populate(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self, hands, per_hand = 1): #метод выдает по 1 карте
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Карты кончились")

#основная часть
def main():
    deck1 = Deck()
    print(deck1) #используется метод __str__() для формирования строчного вывода
    deck1.populate() #перебираются все возможные комбинвции и создаются объукты класса Card
    print(deck1)
    deck1.shuffle() #перемешивание колоды
    print(deck1)
    my_hand = Hand()
    your_hand = Hand()
    hands = [my_hand, your_hand]
    deck1.deal(hands, per_hand = 5) #каждому игроку выдали по 5 карт
    print(my_hand)
    print(your_hand)
    deck1.clear()
    print(deck1)

    input("bb")
main()

