##############################################
#	Assignment 3 - Game Programming - HK181
#
#   Group 4:
#   Pham Quang Minh - 1512016
#   Nguyen Dinh Hao - 1510896
#   Vu Anh Tuan - 1513888
############################################

import pygame as pg
from Classes.Constants import GROUND_DIR, BLACK

class Ground(pg.sprite.Sprite):
    def __init__(self, game, pos_x, pos_y, type = 0):
        self.groups = game.all_sprites, game.grounds
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.ground_list = [pg.transform.scale(pg.image.load(GROUND_DIR + "ground1.png"), (511, 94)),
                            pg.transform.scale(pg.image.load(GROUND_DIR + "ground2.png"), (1022, 94)),
                            pg.transform.scale(pg.image.load(GROUND_DIR + "ground3.png"), (380, 47)),
                            pg.transform.scale(pg.image.load(GROUND_DIR + "ground4.png"), (200, 50))]
        self.image = self.ground_list[type]
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y