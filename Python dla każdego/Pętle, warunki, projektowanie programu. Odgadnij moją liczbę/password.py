# Autor: Maciej Kuta
# Data utworzenie: 6.10.2020
# Cel: Poznanie instrukcji warunkowej if, else

print("Witaj w systemie firmy Bezpieczny Komputer SA")
print("-- bezpieczeństwo to podstawa naszego działania")

password = input("Wprowadź hasło: ")

if password=="sekret":
    print("Dostęp udzielony")
    print("Witaj! Musisz być kimś bardzo ważnym")
else:
    print("Odmowa dostępu")

input("\nNaciśnij klawisz Enter, aby zakończyć działanie programu")