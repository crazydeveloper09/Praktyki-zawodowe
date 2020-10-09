# Autor: Maciej Kuta
# Data utworzenie: 8.10.2020
# Cel: Definiowanie metod i atrybutów prywatnych

class Critter(object):
    total = 0
    @staticmethod
    def status():
        print("\nOgólna liczba zwierzaków to", Critter.total)
    def __init__(self, name, mood):
        print("Urodził się nowy zwierzak")
        self.name = name
        self.__mood = mood
        Critter.total += 1
    def __str__(self):
        print("name:", self.name)
        return self.name
    def public_method(self):
        print("To jest publiczna metoda")
    def __private(self):
        print("To jest prywatna metoda")
    def talk(self):
        print("Cześć! Jestem", self.name)
        print("Jestem teraz", self.__mood)
    
crit = Critter("Zoja", "szczęśliwy")
crit.talk()

crit.public_method()
crit._Critter__private()


print("Wyświetlenie imienia pierwszego zwierzaka: ", crit.name)

input("\n\nNaciśnij klawisz Enter, aby zakończyć program")