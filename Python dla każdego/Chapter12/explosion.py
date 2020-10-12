#!/usr/bin/env python3
# Autor: Maciej Kuta
# Data utworzenie: 12.10.2020
# Cel: Utworzenie animacji
from superwires import games

games.init(screen_width = 640, screen_height = 480, fps=50)


def main():
    mglawica_image = games.load_image("mglawica.jpg", transparent= False)
    games.screen.background = mglawica_image

    explosion_files = ["eksplozja1.bmp",
                    "eksplozja2.bmp",
                    "eksplozja3.bmp",
                    "eksplozja4.bmp",
                    "eksplozja5.bmp",
                    "eksplozja6.bmp",
                    "eksplozja7.bmp",
                    "eksplozja8.bmp",
                    "eksplozja9.bmp"]
    explosion = games.Animation(images = explosion_files, 
                        y=games.screen.height/2, 
                        x=games.screen.width/2,
                        n_repeats = 0,
                        repeat_interval = 5)
    games.screen.add(explosion)

    games.screen.mainloop()

main()