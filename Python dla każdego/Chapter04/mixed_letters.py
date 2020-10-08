# Autor: Maciej Kuta
# Data utworzenie: 7.10.2020
# Cel: Tworzenie wycinka łańcucha
import random

WORDS = ("javascript", "node", "heheszki", "programowanko")

word = random.choice(WORDS)
correct = word
anagram = ""

while word:
    position = random.randrange(len(word))
    anagram += word[position]
    word = word[:position] + word[(position + 1):]

print("Witaj w grze 'Wymieszane litery'")
print("\nUporządkuj litery, aby odtworzyć prawdiłowe słowo")
print("(Aby ukończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)")
print("Zgadnij, jakie to słowo:", anagram)

guess = input("\nTwoja odpowiedź: ")
while guess != correct and guess != "":
    print("Niestety to nie to słowo")
    guess = input("\nTwoja odpowiedź: ")

if guess == correct:
    print("Brawo! Udało się")

print("Dziękuję za udział w grze")




input("\nNaciśnij klawisz Enter, by zakończyć działanie programu")