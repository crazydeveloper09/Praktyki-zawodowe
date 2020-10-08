# Autor: Maciej Kuta
# Data utworzenie: 7.10.2020
# Tytuł: Wymieszane litery 2.0
# Cel: Dodanie podpowiedzi i punktacji

import random

WORDS = ("javascript", "node", "heheszki", "programowanko")
HINTS = ("język programowania", "typ javascript", "reakcja na żart", "programowanie")
word = random.choice(WORDS)
correct = word
anagram = ""
word_index = WORDS.index(word)
while word:
    position = random.randrange(len(word))
    anagram += word[position]
    word = word[:position] + word[(position + 1):]

print("Witaj w grze 'Wymieszane litery'")
print("\nUporządkuj litery, aby odtworzyć prawdiłowe słowo")
print("(Aby ukończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)")
print("Zgadnij, jakie to słowo:", anagram)
tries = 1
points = 100
guess = input("\nTwoja odpowiedź: ")
while guess != correct and guess != "":
    if tries > 5:
        print("Niestety to nie to słowo")
        guess = input("\nTwoja odpowiedź: ")
        points -= 5
        print(HINTS[word_index])
        tries += 1
    else:
        print("Niestety to nie to słowo")
        guess = input("\nTwoja odpowiedź: ")
        tries += 1
   

if guess == correct:
    if tries < 5:
        print("Brawo! Udało się")
        points += 10
    else:
        print("Brawo! Udało się")
    
print("Twoje punkty: ", points)
print("Dziękuję za udział w grze")