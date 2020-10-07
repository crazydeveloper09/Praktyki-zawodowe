# Autor: Maciej Kuta
# Data utworzenie: 7.10.2020
# Tytuł: Zgadywacz słów
# Cel: Losowe wybieranie słów i proszenie o zgadnięcie użytkownika

import random
print("Witaj w grze 'Zgadnij słowo'")
WORDS = ("javascript", "node", "heheszki", "programowanko")

word = random.choice(WORDS)
counter = 1
print("W tym słowie znajduje się", len(word), "liter")
word_help = input("Podaj literę: ")
while counter <= 5:
    if word_help.lower() in word:
        print(word_help, "znajduje się w tym słowie")
    else:
        print(word_help, "nie znajduje się w tym słowie")
    word_help = input("Podaj literę: ")
    counter += 1

 

guess = input("\nTwoja odpowiedź: ")


if guess.lower() == word:
    print("Brawo! Udało się")
else:
    print("Niestety to nie to słowo")

print("Dziękuję za udział w grze")