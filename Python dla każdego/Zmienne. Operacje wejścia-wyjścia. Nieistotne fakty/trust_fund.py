# Autor: Maciej Kuta
# Data utworzenie: 6.10.2020
# Cel: Poprawne używanie zmiennych

print("\t\t Uczestnik funduszu powierniczego")

print("\n Sumuje twoje miesięczne wydatki, żeby Twój fundusz powierniczy" +
    " się nie wyczerpał"
)
print("(bo wtedy byłbyś zmuszony do podjęcia prawdziwej pracy).")

print("Wprowadź swoje wymagane miesięczne koszty. Ponieważ jesteś bogaty" +
     ", zignoruj grosze i swoje koszty podaj w pełnych złotych."
)

mercedes = int(input("Serwis Mercedesa: "))
apartament = int(input("Apartament w Śródmieściu: "))
airplane = int(input("Wynajem prywatnego samolotu: "))
gifts = int(input("Podarunki: "))
dinners = int(input("Obiady w restauracjach: "))
personel = int(input("Personel <służba domowa, kucharz, kierowca, asystent>: "))
coach = int(input("Osobisty guru i coach: "))
games = int(input("Gry komputerowe: "))

print("\nOgółem:", mercedes + apartament + airplane + gifts + dinners + personel + coach + games)

input("\nKliknij klawisz Enter, aby zakończyć program")