#!/usr/bin/env python3
# Autor: Maciej Kuta
# Data utworzenie: 12.10.2020
# Cel: Odczytywanie klawisza klawiatury

from superwires import games

games.init(screen_width = 640, screen_height = 480, fps=50)

class Ship(games.Sprite):
    def update(self):
        if games.keyboard.is_pressed(games.K_w):
            self.y -= 1
        if games.keyboard.is_pressed(games.K_s):
            self.y += 1
        if games.keyboard.is_pressed(games.K_a):
            self.x -= 1
        if games.keyboard.is_pressed(games.K_d):
            self.x += 1

def main():
    mglawica_image = games.load_image("mglawica.jpg", transparent= False)
    games.screen.background = mglawica_image

    ship_image = games.load_image("statek.bmp")
    ship = Ship(image = ship_image, y=games.screen.height/2, x=games.screen.width/2)
    games.screen.add(ship)

    games.screen.mainloop()

main()