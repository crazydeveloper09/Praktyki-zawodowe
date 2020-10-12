#!/usr/bin/env python3
# Autor: Maciej Kuta
# Data utworzenie: 12.10.2020
# Cel: Tworzenie poruszającyh się asteroidów

from superwires import games
import random, math
games.init(screen_width = 640, screen_height = 480, fps=50)

class Asteroid(games.Sprite):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL : games.load_image("asteroida_mala.bmp"),
            MEDIUM : games.load_image("asteroida_sred.bmp"),
            LARGE : games.load_image("asteroida_duza.bmp") }
    SPEED = 2
    def __init__(self, x, y, size):

        super(Asteroid, self).__init__(
                                image = Asteroid.images[size],
                                x = x, y = y,
                                dx = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size,
                                dy = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size)
        self.size = size
    def update(self):
        if self.top > games.screen.height:
            self.bottom = 0
        if self.bottom < 0:
            self.top = games.screen.height
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width

class Ship(games.Sprite):
    image = games.load_image("statek.bmp")
    ROTATION_STEP = 3
    VELOCITY_STEP = .03
    sound = games.load_sound("przyspieszenie.wav")
    def update(self):
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_UP):
            Ship.sound.play()
            angle = self.angle * math.pi / 180
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)
            if self.top > games.screen.height:
                self.bottom = 0
            if self.bottom < 0:
                self.top = games.screen.height
            if self.left > games.screen.width:
                self.right = 0
            if self.right < 0:
                self.left = games.screen.width


def main():
    mglawica_image = games.load_image("mglawica.jpg", transparent= False)
    games.screen.background = mglawica_image

    for i in range(8):
        x = random.randrange(games.screen.width)
        y = random.randrange(games.screen.height)
        size = random.choice([Asteroid.SMALL, Asteroid.MEDIUM, Asteroid.LARGE])
        new_asteroid = Asteroid(x = x, y = y, size= size)
        games.screen.add(new_asteroid)

    ship = Ship(image = Ship.image,
                    x = games.screen.width/2,
                    y = games.screen.height/2)

    games.screen.add(ship)
    games.screen.mainloop()

main()