# Autor: Maciej Kuta
# Data utworzenie: 9.10.2020
# Cel: Modyfikowanie zachowania odziedziczonych metod
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
class Unprintable(Card):
    def __str__(self):
        return "utajniona"
class Positionable(Card):
    def __init__(self, rank, suit, face_up = True):
        super(Positionable, self).__init__(rank, suit)
        self.is_face_up = face_up
    def __str__(self):
        if self.is_face_up:
            rep = super(Positionable, self).__str__()
        else:
            rep = "XX"
        return rep
    def hide(self):
        self.is_face_up = False
ace = Card("A", "c")
unprintable = Unprintable("A", "d")
positionable = Positionable("A", "h")

print("Wyświetlenie obiektu klasy Card")
print(ace)

print("Wyświetlenie obiektu klasy Unprintable")
print(unprintable)

print("Wyświetlenie obiektu klasy Positionable")
print(positionable)
print("Odwrócenie stanu obiektu klasy Positionable")
positionable.hide()
print("Wyświetlenie obiektu klasy Positionable")
print(positionable)
input("\n\nNaciśnij klawisz Enter, aby zakończyć program")