# Autor: Maciej Kuta
# Data utworzenie: 7.10.2020
# Cel: Demonstracja tworzenia krotek

inventory = ()

if not inventory:
    print("Nie posiadasz niczego")

input("\nAby kontynuować kliknij klawisz Enter")

inventory = ("miecz", "zbroja", "tarcza", "napój uzdrawiający")

print("\nWykaz zawartości krotki")
print(inventory)

print("\nElementy twojego wyposażenia: ")
for item in inventory:
    print(item)

input("\nNaciśnij klawisz Enter, by zakończyć działanie programu")