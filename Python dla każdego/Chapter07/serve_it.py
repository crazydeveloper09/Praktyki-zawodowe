# Autor: Maciej Kuta
# Data utworzenie: 8.10.2020
# Cel:Pokazanie obsługi wyjątków

try:
    num = int(input("Wprowadź liczbę: "))
except:
    print("Wystąpił jakiś błąd!")

try:
    num = int(input("\nWprowadź liczbę: "))
except ValueError:
    print("To nie była liczba")

for value in (None, "Hej!"):
    try:
        print("Próba konwersji:", value, "-->", end=" ")
        print(float(value))
    except (TypeError, ValueError):
        print("Wystąpił jakiś błąd!")

for value in (None, "Hej!"):
    try:
        print("Próba konwersji:", value, "-->", end=" ")
        print(float(value))
    except TypeError:
        print("Możliwa jest tylko konwersja łańcucha lub liczby!")
    except ValueError:
        print("Możliwa jest tylko konwersja łańcucha cyfr!")

try:
    num = float(input("\nWprowadź liczbę: "))
except ValueError as e:
    print("To nie była liczba! Lub wyrażając to na sposób Pythona...")
    print(e)

try:
    num = float(input("\nWprowadź liczbę: "))
except ValueError:
    print("To nie była liczba!")
else:
    print("Wprowadziłeś liczbę", num)

input("\n\nNaciśnij klawisz Enter, aby zakończyć działanie programu")