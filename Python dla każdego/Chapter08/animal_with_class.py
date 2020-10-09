# Autor: Maciej Kuta
# Data utworzenie: 8.10.2020
# Cel: Definiowanie liczenia obiektów klasy

class Critter(object):
    total = 0
    @staticmethod
    def status():
        print("\nOgólna liczba zwierzaków to", Critter.total)
    def __init__(self, name):
        print("Urodził się nowy zwierzak")
        self.name = name
        Critter.total += 1
    def __str__(self):
        print("name:", self.name)
        return self.name
    
    def talk(self):
        print("Cześć! Jestem", self.name)
    
crit = Critter("Zoja")
crit1 = Critter("Pimpek")
print(crit)
crit.talk()
crit1.talk()
crit1.status()

print("Wyświetlenie imienia pierwszego zwierzaka: ", crit.name)

input("\n\nNaciśnij klawisz Enter, aby zakończyć program")