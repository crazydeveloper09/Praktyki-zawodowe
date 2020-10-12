#!/usr/bin/env python3
# Autor: Maciej Kuta
# Data utworzenie: 12.10.2020
# Cel: Tworzenie obiektu Message

from superwires import games,color
import pygame

games.init(screen_width = 640, screen_height = 480, fps=50)

wall_image = games.load_image("sciana.jpg")
games.screen.background = wall_image

won_message = games.Message(
                            value="Wygrałeś",
                            size=110,
                            color = color.red,
                            x = games.screen.width/2,
                            y = games.screen.height/2,
                            lifetime = 250,
                            after_death= games.screen.quit
)
games.screen.add(won_message)

games.screen.mainloop()