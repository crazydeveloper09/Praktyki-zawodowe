#!/usr/bin/env python3
# Autor: Maciej Kuta
# Data utworzenie: 12.10.2020
# Cel: Tworzenie elementu tekstu

from superwires import games,color
import pygame

games.init(screen_width = 640, screen_height = 480, fps=50)

wall_image = games.load_image("sciana.jpg")
games.screen.background = wall_image

pizza_image = games.load_image("pizza.bmp")
pizza = games.Sprite(image=pizza_image, x = 390, y = 250)
games.screen.add(pizza)

score = games.Text(
                    value=33,
                    size=20,
                    color=color.black,
                    x=530,
                    y=30
)
games.screen.add(score)

games.screen.mainloop()