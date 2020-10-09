# Autor: Maciej Kuta
# Data utworzenie: 9.10.2020
# Cel: Mój pierwszy moduł


class Player(object):
    def __init__(self, name, score=0):
        self.name = name
        self.score = score
    def __str__(self):
        rep = self.name + "\t" + " " + str(self.score)
        return rep
    
def ask_yes_no(question):
    answer = None
    while answer not in ("t", "n"):
        answer = input(question)
    return answer

def ask_number(question):
    answer = None
    while answer not in range(2, 5):
        answer = int(input(question))
    return answer

if __name__ == "__main__":
    print("Uruchomiłeś ten moduł bezpośrednio (zamiast go zaimportować).")
    input("\n\nNaciśnij klawisz Enter, aby zakończyć działanie programu")