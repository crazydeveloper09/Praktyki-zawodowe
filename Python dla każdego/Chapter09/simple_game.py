# Autor: Maciej Kuta
# Data utworzenie: 9.10.2020
# Cel: Import modułów

import games, random

print("Witaj w najprotszej grze na świecie")

again = None
while again != "n":
    players = []
    num = games.ask_number("Podaj liczbę graczy: ")
    for i in range(num):
        name = input("Nazwa gracza: ")
        score = random.randrange(100) +1
        player = games.Player(name, score)
        players.append(player)

    print("\nOto wyniki gry")
    for player in players:
        print(player)
    again = games.ask_yes_no("Czy chcesz zagrać ponownie? (t/n): ")

input("\n\nNaciśnij klawisz Enter, aby zakończyć działanie programu")