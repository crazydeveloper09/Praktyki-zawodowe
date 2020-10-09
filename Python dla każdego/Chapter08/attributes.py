# Autor: Maciej Kuta
# Data utworzenie: 8.10.2020
# Cel: Definiowanie atrybutów

class Critter(object):
    def __init__(self, name):
        print("Urodził się nowy zwierzak")
        self.name = name
    def __str__(self):
        print("name:", self.name)
        return self.name
    def talk(self):
        print("Cześć! Jestem", self.name)
    
crit = Critter("Zoja")
crit1 = Critter("Pimpek")
crit.talk()
crit1.talk()

print("Wyświetlenie imienia pierwszego zwierzaka: ", crit.name)
print(crit)
input("\n\nNaciśnij klawisz Enter, aby zakończyć program")