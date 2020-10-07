# Autor: Maciej Kuta
# Data utworzenie: 7.10.2020
# Tytuł: Jaka to liczba 2.0
# Cel: Ograniczenie liczby prób do odgadnięcia


import random

print("\t\tWitaj w grze 'Jaka to liczba'")
print("Mam na myśli pewną liczbę z zakresu od 1 do 100")
print("Spróbuj ją odgadnąć w jak najmniejszej liczbie prób")

tries = 1

guess = int(input("Ta liczba to: "))
number = random.randint(1, 100)

while number != guess:
    if tries >= 10:
        print("Niestety nie udało Ci się odgadnąć liczby")
        input("\nNaciśnij przycisk Enter, aby zakończyć działanie programu")
        exit()
    else:
        if guess > number:
            print("Ta liczba jest za duża")
        else:
            print("Ta liczba jest za mała")
        guess = int(input("Ta liczba to: "))
        tries += 1
    

print("Odgadłeś! Ta liczba to", number)
print("Do osiągnięcia sukcesu potrzebowałeś tylko", tries, "prób")


input("\nNaciśnij przycisk Enter, aby zakończyć działanie programu")
