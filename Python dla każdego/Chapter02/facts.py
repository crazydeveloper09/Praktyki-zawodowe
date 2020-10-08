# Autor: Maciej Kuta
# Data utworzenie: 6.10.2020
# Cel: Uzyskanie informacji od użytkownika i wyświetlenie bezużytecznych informacji o nim

name = input("Siema ziom! Jak masz na imię? ")
age = int(input("Ile masz lat? "))
weight = int(input("Łostatnie pytanko. Ile kilogramów ważysz? "))

print("Jeśli poeta ee cummings wysłałby do Ciebie wiadomość e-mail,")
print("zwróciłby się do Ciebie", name.lower())
print("Ale jeśli byłby wściekły, nazwałby Cię", name.upper())

print("\nJeśli małe dziecko próbowałoby zwrócić na siebie Twoją uwagę,")
print("Twoje imię przybrałoby formę:")
print(name * 5)

life = (age * 365) * (24*3600)

print("\nŻyjesz już ponad", life, "sekund")

moon_weight = weight / 6
print("\nCzy wiesz, że na Księżycu Twoja waga wynosiła",
    moon_weight, "kg?")
sun_weight = weight * 27.1
print("Na Słońcu ważyłbyś (ważyłabyś)", sun_weight, "kg (ale niestety niedługo)")

input("\nKliknij klawisz Enter, aby zakończyć program")