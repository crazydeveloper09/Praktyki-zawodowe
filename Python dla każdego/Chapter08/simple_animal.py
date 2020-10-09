# Autor: Maciej Kuta
# Data utworzenie: 8.10.2020
# Cel: Definiowanie klasy

class Critter(object):
    def talk(self):
        print("Cześć!Jestem egzemplarzem klasy Critter")
    
crit = Critter()
crit.talk()

input("\n\nNaciśnij klawisz Enter, aby zakończyć program")