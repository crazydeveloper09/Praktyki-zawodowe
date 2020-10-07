# Autor: Maciej Kuta
# Data utworzenie: 7.10.2020
# Tytuł: Wczytaj i wyświetl
# Cel: Wczytanie komunikatu i wyświetlenie go w odwrotnej kolejności

message= input("Podaj swój komunikat: ")
print("Twój komunikat w odwrotnej kolejności brzmi:")
for letter in range(len(message) -1, -1, -1):
    print(message[letter], end="")
    print(message[letter])


input("\nNaciśnij klawisz Enter, by zakończyć działanie programu")