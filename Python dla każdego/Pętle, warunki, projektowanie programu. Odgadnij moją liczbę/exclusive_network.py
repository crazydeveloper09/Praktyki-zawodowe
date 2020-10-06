# Autor: Maciej Kuta
# Data utworzenie: 6.10.2020
# Cel: Demonstruje warunki złożone i operatory

print("Witaj w eksluzywnej sieci")

username=""

while not username:
    username = input("Nazwa użytkownika: ")

password = ""

while not password:
    password =  input("Hasło: ")

if username=="Maciek" and password=="developer":
    print("Co tam u Ciebie", username)
elif username=="Moja siostra" and password=="brother":
     print("Co tam u Ciebie", username)
elif username=="gość" or password=="gość":
    print("Witaj, gościu")
else:
    print("Nie mamy takiego użytkownika w bazie")

input("\nNaciśnij przycisk Enter, aby zakończyć działanie programu")