#!/usr/bin/env python3
# Autor: Maciej Kuta
# Data utworzenie: 12.10.2020
# Cel: Tworzenie okna graficznego z tłem 

from superwires import games
import pygame

games.init(screen_width = 640, screen_height = 480, fps=50)

wall_image = games.load_image("sciana.jpg")
games.screen.background = wall_image

games.screen.mainloop()