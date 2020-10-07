# Autor: Maciej Kuta
# Data utworzenie: 7.10.2020
# Cel: Demonstracja metod listy

geek = {"404": "ignorant; od używanego w sieci WWW komunikatu o błędzie 404\n - nie znaleziono strony.",
        "Googling": "googlowanie; wyszukiwanie w internecie informacji dotyczących jakiejś osoby.",
        "Keyboard Plaque" : "(skojarzone z kamieniem nazębnym)zanieczyszczenia nagromadzone w klawiaturze komputera.",
        "Link Rot" : "(obumieranie linków) proces, w  wyniku którego linki do stron WWW stają się nieaktualne.",
        "Percussive Maintenance" : "(konserwacja perkusyjna)naprawa urządzenia elektronicznego przez stuknięcie.",
        "Uninstalled" : "(odinstalowany) zwolniony z pracy;  termin szczególnie popularny w okresie bańki internetowej."}  
choice = None

while choice != "0":
    print("Translator slangu komputerowego\n")
    print("""
        0 - zakończ
        1 - znajdź termin
        2 - dodaj nowy termin
        3 - zmień definicję terminu
        4 - usuń termnin
        """
    )
    choice = input("Wybierasz: ")
    if choice == "0":
        print("Do widzenia")
    elif choice == "1":
        term = input("Jaki termin mam przetłumaczyć?: ")
        if term in geek:
            definition = geek[term]
            print("\n", term, "oznacza", definition)
        else:
            print("\nNiestety, nie znam terminu", term)
   
    elif choice == "2":
        term = input("Podaj nazwę terminu: ")
        if term not in geek:
            definiition = input("Podaj jego definicję: ")
            geek[term] = definiition
        else:
            print("Ten termin już jest w słowniku")
        
    elif choice == "3":
        term = input("Jakiego terminu definicję chciałbyś zmienić? ")
        if term in geek:
            definition = input("Jaka jest nowa definicja? ")
            geek[term] = definition
        else:
            print("Ten termin nie istnieje")
    elif choice == "4":
        term = input("Jaki termin chciałbyś usunąć? ")
        if term in geek:
            del geek[term]
        else:
            print("Ten termin nie istnieje")
    else:
        print("Nie ma takiego polecenia w menu")

input("\nNaciśnij klawisz Enter, by zakończyć działanie programu")