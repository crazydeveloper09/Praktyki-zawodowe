# Autor: Maciej Kuta
# Data utworzenie: 7.10.2020
# Cel: Demonstracja operacji na listach


inventory = ["miecz", "zbroja", "tarcza", "napój uzdrawiający"]


print("\nElementy twojego wyposażenia: ")
for item in inventory:
    print(item)

input("\nNaciśnij klawisz Enter, by kontynuować działanie programu")
print("Twój dobytek zawiera", len(inventory), "elementy(-ów)")

input("\nNaciśnij klawisz Enter, by kontynuować działanie programu")
if "napój uzdrawiający" in inventory:
    print("Dożyjesz dnia, w którym stoczysz walkę.")

index = int(input("\nWprowadź indeks elementu inwentarza: "))
print("Pod indeksem", index, "znajduje się", inventory[index])

begin = int(input("\nWprowadź indeks wyznaczjący początek wycinka: "))
end = int(input("\nWprowadź indeks wyznaczjący koniec wycinka: "))
print("inventory[", begin, ":", end, "] to", inventory[begin:end])

input("\nNaciśnij klawisz Enter, by kontynuować działanie programu")
print("Znajdujesz skrzynię, która zawiera:")

print("Dodajesz zawartość skrzyni do swojego inwentarza")
inventory.append(["złoto", "klejnoty"])

print("Twój aktualny inwentarz to:")
print(inventory)

input("\nNaciśnij klawisz Enter, by kontynuować działanie programu")
print("Wymieniasz swój miecz na kuszę")
inventory.remove("miecz")
inventory.append("kusza")
print("Twój aktualny inwentarz to:")
print(inventory)

input("\nNaciśnij klawisz Enter, by kontynuować działanie programu")
print("Zużywasz swoje złoto i klejnoty na zakup kuli do wrózenia")
inventory.remove(["złoto", "klejnoty"])
inventory.append("kule do wrózenia")
print("Twój aktualny inwentarz to:")
print(inventory)

input("\nNaciśnij klawisz Enter, by kontynuować działanie programu")
print("W wielkiej bitwie tarcza zostaje zniszczona")
inventory.remove("tarcza")
print("Twój aktualny inwentarz to:")
print(inventory)

input("\nNaciśnij klawisz Enter, by kontynuować działanie programu")
print("Twoja kusza i zbroja zostały skradzione przez złodziei")
del inventory[:2]
print("Twój aktualny inwentarz to:")
print(inventory)

input("\nNaciśnij klawisz Enter, by zakończyć działanie programu")