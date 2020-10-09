# Autor: Maciej Kuta
# Data utworzenie: 8.10.2020
# Cel: Definiowanie konstruktora

class Critter(object):
    def __init__(self):
        print("Urodził się nowy zwierzak")
    def talk(self):
        print("Cześć!Jestem egzemplarzem klasy Critter")
    
crit = Critter()
crit1 = Critter()
crit.talk()
crit1.talk()

input("\n\nNaciśnij klawisz Enter, aby zakończyć program")