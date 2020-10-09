# Autor: Maciej Kuta
# Data utworzenie: 9.10.2020
# # Cel: Komunikacja między klasą bazową, a pochodną
class Card(object):
    total = 0
    RANKS = ["A", "2", "3", "4", "5", "6", "7","8",
            "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        Card.total += 1
    
    def __str__(self):
        rep = self.rank + self.suit
        return rep
class Hand(object):
    def __init__(self):
        self.cards = []
    def __str__(self):
        if len(self.cards) == 0:
            rep="(pusta)"
            
        else:
            rep=""
            for card in self.cards:
                rep+= str(card) + " "
        return rep

    def add_card(self, card):
        
        self.cards.append(card)
        
      
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add_card(card)

class Deck(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add_card(Card(rank, suit))
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Nie mogę dalej rozdawać")

mine = Hand()
your = Hand()
print("Utworzyłem nową talię kart")
deck1 = Deck()
print("Talia:")
print(deck1)

print("\nDodałem do talli komplet kart")
deck1.populate()
print("Talia:")
print(deck1)

print("\nPotasowałem talię kart")
deck1.shuffle()
print("Talia:")
print(deck1)

print("\nRozdałem sobie i Tobie po 5 kart")
hands = [mine, your]
deck1.deal(hands, per_hand=5)
print("Moja ręka:")
print(mine)
print("Twoja ręka:")
print(your)
print("Talia:")
print(deck1)

input("\n\nNaciśnij klawisz Enter, aby zakończyć program")