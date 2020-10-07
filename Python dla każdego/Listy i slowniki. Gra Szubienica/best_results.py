# Autor: Maciej Kuta
# Data utworzenie: 7.10.2020
# Cel: Demonstracja metod listy

scores = []
choice = None

while choice != "0":
    print("""
        0 - zakończ
        1 - pokaż wyniki
        2 - dodaj wynik
        3 - usuń wynik
        4 - posortuj wyniki
        """
    )
    choice = input("Wybierasz: ")
    if choice == "0":
        print("Do widzenia")
    elif choice == "1":
        for item in scores:
            print(item)
    elif choice == "2":
        score = int(input("Jaki wynik uzyskałeś? "))
        scores.append(score)
    elif choice == "3":
        score = int(input("Jaki wynik chcesz usunąć? "))
        if score in scores:
            scores.remove(score)
        else:
            print(score, "nie ma na liście wyników")
    elif choice == "4":
        scores.sort(reverse=True)
    else:
        print("Nie ma takiego polecenia w menu")

input("\nNaciśnij klawisz Enter, by zakończyć działanie programu")