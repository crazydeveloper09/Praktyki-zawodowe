# Autor: Maciej Kuta
# Data utworzenie: 6.10.2020
# Cel: Umyślne tworzenie pętli nieskończonych

count = 0

while True: 
    count += 1
    if count >= 10:
        break
    if count == 5:
        continue
    print(count)

input("\nNaciśnij klawisz Enter, by zakończyć działanie programu")
