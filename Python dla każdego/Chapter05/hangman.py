# Autor: Maciej Kuta
# Data utworzenie: 7.10.2020
# Cel: ćwiczenia na słownikach i listach

import random

tries = 0
words = ["PYTHON", "JAVASCRIPT", "JAVA"]
word = random.choice(words)
passwd = "-" * len(word)
used = []


print("Witaj w szubienicy")
print("Hasło ma", len(word), "liter")
print(passwd)

while tries < 13 and passwd != word:
    letter = input("Podaj literę: ")
    while letter in used:
        print("Już wykorzystałeś literę", letter)
        letter = input("Podaj literę: ")
    used.append(letter)
    if letter.upper() in word:
        print("Zgadłeś literę")
        
        print("Te litery zostały już użyte")
        print(used)
        new = ""
        for i in range(len(word)):
            if letter.upper() == word[i]:
                new += letter.upper()
            else:
                new += passwd[i]

        passwd = new
        print(new)
    else:
        print("Nie ma tej litery! Próbuj dalej")
        
    
    tries += 1
    print("Pozostało", 13 - tries, "prób")
if passwd == word:
    print("Odgadłeś słowo", word, "w", tries, "prób")
else:
    print("Nue udało Ci się odgadnąć słowa")


input("\nNaciśnij klawisz Enter, by zakończyć działanie programu")