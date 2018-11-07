##############################################
#	Assignment 3 - Game Programming - HK181
#
#   Group 4:
#   Pham Quang Minh - 1512016
#   Nguyen Dinh Hao - 1510896
#   Vu Anh Tuan - 1513888
############################################

import pygame as pg
from random import choice, randrange
from Classes.Constants import CLOUD_DIR, BLACK
vec = pg.math.Vector2

class Cloud(pg.sprite.Sprite):
    def __init__(self, game, distance):
        self.groups = game.all_sprites, game.clouds
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.cloud_list = [pg.image.load(CLOUD_DIR + "cloud1.png"),
                            pg.image.load(CLOUD_DIR + "cloud2.png"),
                            pg.image.load(CLOUD_DIR + "cloud3.png")]

        self.image = choice(self.cloud_list)
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = 500 * (distance + 1)
        self.rect.y = randrange(100, 400)
        self.pos = vec(self.rect.x, self.rect.y) # Position of cloud
        self.movx = choice([-0.5, -0.4, -0.3, -0.2, 0.2, 0.3, 0.4, 0.5]) # Move of cloud

    def update(self):
        self.pos.x = self.pos.x + self.movx
        self.rect.center = self.pos

        if self.pos.x < -200 or self.pos.x > 15200:
            self.kill() 