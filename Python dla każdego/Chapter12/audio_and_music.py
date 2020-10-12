# Autor: Maciej Kuta
# Data utworzenie: 12.10.2020
# Cel: Demonstracja metod listy
from superwires import games
import pygame
from pygame import mixer

pygame.init()

games.init(screen_width = 640, screen_height = 480, fps=50)
pygame.mixer.init()
missile_sound = mixer.music.load("pocisk.wav")
topic = mixer.music.load("temat.mid")



choice = None

while choice != "0":
    print("""
        0 - zakończ
        1 - odtwórz dźwięk pocisku
        2 - odtwarzaj cyklicznie dźwięk pocisku
        3 - zatrzymaj odtwarzanie dźwięku pocisku
        4 - odtwórz temat muzyczny
        5 - odtwarzaj cyklicznie tematu muzycznego
        6 - zatrzymaj odtwarzanie tematu muzycznego
        """
    )
    choice = input("Wybierasz: ")
    if choice == "0":
        print("Do widzenia")
    elif choice == "1":
        missile_sound.play()
        print("Odtwarzasz dźwięk pocisku")
    elif choice == "2":
        loop = int(input("Ile razy powtórzyć odtwarzanie? (-1 = bez końca): "))
        missile_sound.play(loop)
        print("Cykliczne odtwarzanie dźwięku pocisku.")
    elif choice == "3":
        missile_sound.stop()
        print("Zatrzymanie odtwarzania dźwięku pocisku.")
    elif choice == "4":
        games.music.play()
        print("Odtworzenie tematu muzycznego.")
    elif choice == "5":
        loop = int(input("Ile razy powtórzyć odtwarzanie? (-1 = bez końca): "))
        games.music.play(loop)
        print("Cykliczne odtwarzanie tematu muzycznego.")
    elif choice == "6":
        games.music.stop()
        print("Zatrzymanie odtwarzania tematu muzycznego.")
    else:
        print("Nie ma takiego polecenia w menu")

input("\nNaciśnij klawisz Enter, by zakończyć działanie programu")