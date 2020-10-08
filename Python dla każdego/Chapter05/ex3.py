# Autor: Maciej Kuta
# Data utworzenie: 8.10.2020
# Tytuł: Kto jest moim tatą
# Cel: Ćwiczenie słowników


father = {}  
choice = None

while choice != "0":
    print("Kto jest moim tatą?\n")
    print("""
        0 - zakończ
        1 - znajdź ojca
        2 - dodaj nową parę syn-ojciec
        3 - zmień imię i nazwisko ojca
        4 - usuń parę syn-ojciec
        """
    )
    choice = input("Wybierasz: ")
    if choice == "0":
        print("Do widzenia")
    elif choice == "1":
        son = input("Podaj imię i nazwisko syna: ")
        if son in father:
            name = father[son]
            print("\n", son, "ma tatę", name)
        else:
            print("\nNiestety, nie znam syna", son)
   
    elif choice == "2":
        son = input("Podaj imię i nazwisko syna: ")
        if son not in father:
            name = input("Podaj imię i nazwisko ojca: ")
            father[son] = name
        else:
            print("Ta para syn-ojciec już istnieje")
        
    elif choice == "3":
        son = input("Dla którego syna chciałbyś zmienić imię i nazwisko ojca? ")
        if son in father:
            name = input("Jakie jest nowe imię i nazwisko ojca? ")
            father[son] = name
        else:
            print("Ta para syn-ojciec nie istnieje")
    elif choice == "4":
        son = input("Jakiego syna chciałbyś usunąć? ")
        if son in father:
            del father[son]
        else:
            print("Ta para syn-ojciec nie istnieje")
    else:
        print("Nie ma takiego polecenia w menu")

input("\nNaciśnij klawisz Enter, by zakończyć działanie programu")