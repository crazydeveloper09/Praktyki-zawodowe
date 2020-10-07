# Autor: Maciej Kuta
# Data utworzenie: 7.10.2020
# Tytuł: Liczydło
# Cel: Liczenie za użytkownika

begin = int(input("Wprowadź liczbę początkową: "))
end = int(input("Wprowadź liczbę końcową: "))
odstep = int(input("Wprowadź liczbę odstępową: "))

while begin <= end:
    print(begin)
    begin+= odstep



input("\nNaciśnij klawisz Enter, by zakończyć działanie programu")