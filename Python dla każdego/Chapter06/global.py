# Autor: Maciej Kuta
# Data utworzenie: 8.10.2020
# Cel: Demonstracja globalności lokalności
value = 10
def read_global(value):
    print("\nWartość zmiennej odczytywana wewnątrz zakresu lokalnego funkcji" +
    " read_global() wynosi: ", value
    )

def shadow_global(value):
    value = -10
    print("\nWartość zmiennej odczytywana wewnątrz zakresu lokalnego funkcji" +
    " shadow_global() wynosi: ", value
    )

def change_global():
    global value
    value = -10
    print("\nWartość zmiennej odczytywana wewnątrz zakresu lokalnego funkcji" +
    " change_global() wynosi: ", value
    )

print("W zakresie globalnym wartość zmiennej value została ustawiona na:", value)

read_global(value)
print("Po powrocie do zakresu globalnego wartość zmiennej value nadal wynosi:", value)

shadow_global(value)
print("Po powrocie do zakresu globalnego wartość zmiennej value nadal wynosi:", value)

change_global()
print("Po powrocie do zakresu globalnego wartość zmiennej value zmieniła się na:", value)

input("\n\nNaciśnij klawisz Enter, aby zakończyć działanie programu")