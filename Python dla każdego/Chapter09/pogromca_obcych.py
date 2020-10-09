# Autor: Maciej Kuta
# Data utworzenie: 9.10.2020
# Cel: Komunikacja między obiektami
class Alien(object):
    def __init__(self, name):
        self.name = name
    def die(self):
        print(self.name, "z trudem łapie oddech, 'To już koniec. Ale wielki koniec...'\n" +
            "Tak robi się ciemno.\t Powiedz moim dwóm milionom larw, że je kochałem\n" +
            "Żegnaj, okrutny wszechświecie"
        )
invader = Alien("Obcy")

class Player(object):
    def __init__(self, name):
        self.name = name
    def blast(self, invader):
        print(self.name, "razi wroga\n")
        invader.die()
    def talk(self):
        print("Cześć!Jestem egzemplarzem klasy Player")
    
hero = Player("Gracz")
hero.blast(invader)

input("\n\nNaciśnij klawisz Enter, aby zakończyć program")