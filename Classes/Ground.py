##############################################
#	Assignment 3 - Game Programming - HK181
#
#   Group 4:
#   Pham Quang Minh - 1512016
#   Nguyen Dinh Hao - 1510896
#   Vu Anh Tuan - 1513888
############################################

import pygame as pg
from Classes.Constants import *

class Ground(pg.sprite.Sprite):
    def __init__(self, game, x, y, type = 0):
        self.groups = game.all_sprites, game.grounds
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        images = [pg.image.load("./Resources/Sprites/ground1.png"),
                  pg.image.load("./Resources/Sprites/ground2.png"),
                  pg.image.load("./Resources/Sprites/ground3.png"),
                  pg.image.load("./Resources/Sprites/ground4.png")]
        self.image = images[type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #if randrange(100) < POW_SPAWN_PCT:
            #Pow(self.game, self)