# Autor: Maciej Kuta
# Data utworzenie: 7.10.2020
# Cel: Demonstracja sekwencji zagnieżdżónych

scores = []
choice = None

while choice != "0":
    print("""
        0 - zakończ
        1 - pokaż wyniki
        2 - dodaj wynik
        """
    )
    choice = input("Wybierasz: ")
    if choice == "0":
        print("Do widzenia")
    elif choice == "1":
        print("IMIĘ \t\t\t WYNIK")
        for item in scores:
            print(item[1],"\t\t\t", item[0])
    elif choice == "2":
        score = int(input("Jaki wynik uzyskałeś? "))
        name = input("Wpisz swoje imię: ")
        scores.append([score, name])
    else:
        print("Nie ma takiego polecenia w menu")

input("\nNaciśnij klawisz Enter, by zakończyć działanie programu")