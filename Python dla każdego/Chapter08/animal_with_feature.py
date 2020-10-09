# Autor: Maciej Kuta
# Data utworzenie: 8.10.2020
# Cel: Definiowanie właściwości

class Critter(object):
    total = 0
    @staticmethod
    def status():
        print("\nOgólna liczba zwierzaków to", Critter.total)
    def __init__(self, name):
        print("Urodził się nowy zwierzak")
        self.__name = name
        Critter.total += 1
    def __str__(self):
        print("name:", self.__name)
        return self.__name
    @property
    def name(self):
        return self.__name
    def talk(self):
        print("Cześć! Jestem", self.name)
    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Pusty łańcuch znaków nie może być imieniem zwierzaka")
        else:
            self.__name = new_name
            print("Zmiana się powiodła")
    
crit = Critter("Zoja")
crit.talk()

crit.name = "Pucek"
crit.talk()

new_name = input("Wprowadź nowę imię ")
crit.name = new_name
crit.talk()


input("\n\nNaciśnij klawisz Enter, aby zakończyć program")