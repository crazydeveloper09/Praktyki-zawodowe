# Autor: Maciej Kuta
# Data utworzenie: 7.10.2020
# Cel: Poznanie funkcji range

print("Liczenie: ")
for normal_counter in range(10):
    print(normal_counter, end=" ")
print("\nLiczenie co pięć: ")
for counter5 in range(0,50,5):
    print(counter5, end=" ")


print("\nLiczenie do tyłu: ")
for reverse in range(10, 0, -1):
    print(reverse, end=" ")


input("\nNaciśnij klawisz Enter, aby zakończyć działanie programu")