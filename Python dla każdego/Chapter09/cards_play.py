# Autor: Maciej Kuta
# Data utworzenie: 9.10.2020
# Cel: Komunikacja między obiektami
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
ace = Card("A", "c")
two = Card("2", "c")
three = Card("3", "c")
four = Card("4", "c")
five = Card("5", "c")

class Hand(object):
    def __init__(self, name):
        self.name = name
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
    def talk(self):
        print(self.name)
    
mine = Hand("Moja ręka")

print("Wyświetlam obiekt karty")
print(ace)

print("Wyświetlam resztę obiektów po jednym na raz")
print(two)
print(three)
print(four)
print(five)

print("Wyświetlam zawartość mojej ręki przed dodaniem jakich kart")
print(mine)

print("Wyświetlam zawartość mojej ręki przed dodaniem jakich kart")
mine.add_card(ace)
mine.add_card(two)
mine.add_card(three)
mine.add_card(four)
mine.add_card(five)
print(mine)
print("Przekazuję pierwsze dwie karty z mojej ręki do Twojej")
your_hand = Hand("Twoja ręka")
mine.give(ace, your_hand)
mine.give(two, your_hand)
your_hand.talk()
print(your_hand)
mine.talk()
print(mine)

input("\n\nNaciśnij klawisz Enter, aby zakończyć program")