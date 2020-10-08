# Autor: Maciej Kuta
# Data utworzenie: 6.10.2020
# Cel: Przećwiczenie  wiedzy z warunków i pętli

import random

print("\t\tWitaj w grze 'Jaka to liczba'")
print("Mam na myśli pewną liczbę z zakresu od 1 do 100")
print("Spróbuj ją odgadnąć w jak najmniejszej liczbie prób")

tries = 1;
guess = int(input("Ta liczba to: "))
number = random.randint(1, 100)

while number != guess:
   
    if guess > number:
        print("Ta liczba jest za duża")
    else:
        print("Ta liczba jest za mała")
    guess = int(input("Ta liczba to: "))
    tries += 1

print("Odgadłeś! Ta liczba to", number)
print("Do osiągnięcia sukcesu potrzebowałeś tylko", tries, "prób")

input("\nNaciśnij przycisk Enter, aby zakończyć działanie programu")
