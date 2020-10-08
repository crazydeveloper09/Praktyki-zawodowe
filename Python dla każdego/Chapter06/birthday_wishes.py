# Autor: Maciej Kuta
# Data utworzenie: 8.10.2020
# Cel: Demonstracja domyślnych wartości parametrów

def birthday1(name, age):
    print("Szczęsliwych urodzin", name, "! Masz już", age, "lat")

def birthday2(name="Przykład", age="5"):
    print("Szczęsliwych urodzin", name, "! Masz już", age, "lat")

birthday1("Janek", 6)
birthday2()

input("\nNaciśnij klawisz Enter, aby zakończyć działanie programu")