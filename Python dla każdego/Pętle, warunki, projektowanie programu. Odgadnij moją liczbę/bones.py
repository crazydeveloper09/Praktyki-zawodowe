# Autor: Maciej Kuta
# Data utworzenie: 6.10.2020
# Cel: Zapoznanie z metodą randrange() i randint()

import random

print("Rzucam kośćmi......")

num1 = random.randint(1, 6)
num2 = random.randrange(1, 6)

print("Wyrzuciłeś", num1, "oraz", num2, "i uzyskałeś sumę", num1 + num2)

input("\nNaciśnij przycisk Enter, aby zakończyć działanie programu")

