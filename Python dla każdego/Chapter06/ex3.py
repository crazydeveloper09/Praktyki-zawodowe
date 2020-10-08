# Autor: Maciej Kuta
# Data utworzenie: 8.10.2020
# Tytuł: Randomowe słowa
# Cel: Przypadkowe wyświetlanie słów z listy

# Autor: Maciej Kuta
# Data utworzenie: 8.10.2020
# Tytuł: Jaka to liczba? 4.0
# Cel: Zmodyfikowanie poprzedniej wersji w celu użycia funkcji main

import random
def ask_number(question):
    answer = None
    
    while answer not in range(1, 100):
        answer = int(input(question))
    return answer
def main():

    print("\t\tWitaj w grze 'Jaka to liczba'")
    print("Mam na myśli pewną liczbę z zakresu od 1 do 100")
    print("Spróbuj ją odgadnąć w jak najmniejszej liczbie prób")

    tries = 1;
    guess = ask_number("Ta liczba to: ")
    number = random.randint(1, 100)

    while number != guess:
    
        if guess > number:
            print("Ta liczba jest za duża")
        else:
            print("Ta liczba jest za mała")
        guess = ask_number("Ta liczba to: ")
        tries += 1

    print("Odgadłeś! Ta liczba to", number)
    print("Do osiągnięcia sukcesu potrzebowałeś tylko", tries, "prób")

main()

input("\nNaciśnij przycisk Enter, aby zakończyć działanie programu")
