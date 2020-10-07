# Autor: Maciej Kuta
# Data utworzenie: 7.10.2020
# Tytuł: Orzeł czy reszka
# Cel: Rzucanie monetą i sprawdzenie czy orzeł czy reszka
import random
counter = 1
orzel = 1
reszka = 1
moneta = random.randint(0,1)

print("Witaj w grze 'Orzeł czy reszka'. Sprawdźmy czego jest więcej")

while counter <= 100:
    moneta = random.randint(0,1)
    if moneta == 0:
        orzel += 1
    else:
        reszka += 1
    counter += 1
    

print("Orzeł ma", orzel, "punktów")
print("Reszka ma", reszka, "punktów")

input("\nNaciśnij przycisk Enter, aby zakończyć działanie programu")



