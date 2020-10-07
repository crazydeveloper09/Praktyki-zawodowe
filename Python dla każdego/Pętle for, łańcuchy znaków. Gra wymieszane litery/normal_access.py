# Autor: Maciej Kuta
# Data utworzenie: 7.10.2020
# Cel: Demostracja indeksowania
import random

word = "indeks"

print("Wartość zmiennej word to: ", word)

high = len(word)
low = -len(word)

for i in range(10):
    position = random.randrange(low, high)
    print("word[", position, "]", word[position])




input("\nNaciśnij klawisz Enter, by zakończyć działanie programu")