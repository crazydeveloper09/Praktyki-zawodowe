#!/usr/bin/env python3
# Autor: Maciej Kuta
# Data utworzenie: 12.10.2020
# Cel: Tworzenie elementu pizzy

from superwires import games
import pygame

games.init(screen_width = 640, screen_height = 480, fps=50)

wall_image = games.load_image("sciana.jpg")
games.screen.background = wall_image

pizza_image = games.load_image("pizza.bmp")
pizza = games.Sprite(image=pizza_image, x = 390, y = 250)
games.screen.add(pizza)

games.screen.mainloop()