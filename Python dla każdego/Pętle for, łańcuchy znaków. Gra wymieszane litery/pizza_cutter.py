# Autor: Maciej Kuta
# Data utworzenie: 7.10.2020
# Cel: Tworzenie wycinka łańcucha

print("Wprowadź początkowy i końcowy indeks wycinka łańcucha 'pizza'.")
print("Aby zakończyć tworzenie wycinków, w odpowiedzi na monit 'Początek:'")
print("naciśnij klawisz Enter.")

word = "pizza"

begin = None
while begin != "":
    begin = (input("Początek: "))
    if begin:
        begin = int(begin)
        end = int(input("Koniec: "))
        print("word[", begin, ":", end, "]", word[begin:end])



input("\nNaciśnij klawisz Enter, by zakończyć działanie programu")