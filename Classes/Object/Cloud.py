##############################################
#	Assignment 3 - Game Programming - HK181
#
#   Group 4:
#   Pham Quang Minh - 1512016
#   Nguyen Dinh Hao - 1510896
#   Vu Anh Tuan - 1513888
############################################

import pygame as pg
from random import choice
from Classes.Constants import CLOUD_DIR, BLACK

class Cloud(pg.sprite.Sprite):
    def __init__(self, game, pos_x, pos_y):
        self.groups = game.all_sprites, game.clouds
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.cloud_list = [pg.transform.scale(pg.image.load(CLOUD_DIR + "cloud1.png"), (511, 94)),
                            pg.transform.scale(pg.image.load(CLOUD_DIR + "cloud2.png"), (511, 94)),
                            pg.transform.scale(pg.image.load(CLOUD_DIR + "cloud3.png"), (511, 94))]
        self.image = choice(self.cloud_list)
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def update(self):
        pass