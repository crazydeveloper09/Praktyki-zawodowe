#!/usr/bin/env python3
# Autor: Maciej Kuta
# Data utworzenie: 12.10.2020
# Cel: Odczytywanie klawisza klawiatury i obracanie elementu

from superwires import games

games.init(screen_width = 640, screen_height = 480, fps=50)

class Ship(games.Sprite):
    def update(self):
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += 1
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= 1



        if games.keyboard.is_pressed(games.K_1):
            self.angle = 0
        if games.keyboard.is_pressed(games.K_2):
            self.angle = 90
        if games.keyboard.is_pressed(games.K_3):
            self.angle = 180
        if games.keyboard.is_pressed(games.K_4):
            self.angle = 270

def main():
    mglawica_image = games.load_image("mglawica.jpg", transparent= False)
    games.screen.background = mglawica_image

    ship_image = games.load_image("statek.bmp")
    ship = Ship(image = ship_image, y=games.screen.height/2, x=games.screen.width/2)
    games.screen.add(ship)

    games.screen.mainloop()

main()