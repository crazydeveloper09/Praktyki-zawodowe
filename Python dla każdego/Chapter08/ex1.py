# Autor: Maciej Kuta
# Data utworzenie: 9.10.2020
# Tytuł: Opiekun zwierzaka 2.0
# Cel: Dodanie tego, że użytkownik może kontrolować poziom głodu

class Critter(object):
    total = 0
    @staticmethod
    def status():
        print("\nOgólna liczba zwierzaków to", Critter.total)
    def __init__(self, name, hunger = 0, boredom = 0):
        print("Urodził się nowy zwierzak")
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        Critter.total += 1
    def __str__(self):
        print("name:", self.name)
        return self.name
    def __pass_time(self):
        self.hunger +=1
        self.boredom += 1
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "szczęśliwy"
        elif 5 <= unhappiness <= 10:
            m = "zadowolony"
        elif 10 <= unhappiness <= 15:
            m = "podenerwowany"
        else:
            m = "wściekły"
        return m

    def talk(self):
        print("Cześć! Nazywam się", self.name, "i jestem", self.mood, "teraz")
        self.__pass_time
    def eat(self, food):
        print("Ale pyszne")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time
    def play(self, fun):
        print("Dziękuję, że się ze mną pobawiłeś")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time
   
def main():
    name = input("Jak chesz nazwać swojego zwierzaka? ")
    animal = Critter(name, 0, 0)

    choice = None  
    while choice != "0":
        print("""
            0 - zakończ
            1 - słuchaj swojego zwierzaka
            2 - nakarm swojego zwierzaka
            3 - pobaw się ze swoim zwierzakiem
            """
        )
        choice = input("Wybierasz: ")
        if choice == "0":
            print("Do widzenia")
        elif choice == "1":

            animal.talk()   
        elif choice == "2":
            try:
                eat_level = int(input("Podaj poziom najedzenia: "))
            except ValueError:
                print("To musi być liczba")
                eat_level = int(input("Podaj poziom najedzenia: "))
                animal.eat(eat_level)
            else:
                animal.eat(eat_level)
        elif choice == "3":
            try:
                fun_level = int(input("Podaj poziom zabawy: "))
            except ValueError:
                print("To musi być liczba")
                fun_level = int(input("Podaj poziom zabawy: "))
                animal.play(fun_level)
            else:
                animal.play(fun_level)
        else:
            print("Nie ma takiego czegoś w menu")
main()
input("\n\nNaciśnij klawisz Enter, aby zakończyć program")