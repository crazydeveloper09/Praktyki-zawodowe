#!/usr/bin/env python3
# Autor: Maciej Kuta
# Data utworzenie: 12.10.2020
# Cel: SOdczytywanie danych wejsciowych z myszy

from superwires import games
import pygame

games.init(screen_width = 640, screen_height = 480, fps=50)

wall_image = games.load_image("sciana.jpg")
games.screen.background = wall_image

class Pan(games.Sprite):
    def update(self):
       self.x = games.mouse.x
       self.y = games.mouse.y

pan_image = games.load_image("patelnia.bmp")
pan = Pan(image=pan_image, 
                    x = games.mouse.x,
                    y = games.mouse.y)
games.screen.add(pan)
games.mouse.is_visible = False
games.screen.event_grab = True


games.screen.mainloop()