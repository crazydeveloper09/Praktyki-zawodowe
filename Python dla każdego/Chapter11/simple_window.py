#!/usr/bin/env python3
# Autor: Maciej Kuta
# Data utworzenie: 12.10.2020
# Cel: Tworzenie nowego okna graficznego

from superwires import games

games.init(screen_width = 640, screen_height = 480, fps=50)

games.screen.mainloop()