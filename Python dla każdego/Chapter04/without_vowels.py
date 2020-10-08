# Autor: Maciej Kuta
# Data utworzenie: 7.10.2020
# Cel: Tworzenie nowego łańcucha
message = input("Wprowadź nowy komunikat: ")
VOWELS = 'aąeęioóuy'
new_message = ""

for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print("Został utworzony nowy łańcuch:, ", new_message)

print("Twój komunikat bez samogłosek to: ", new_message)




input("\nNaciśnij klawisz Enter, by zakończyć działanie programu")