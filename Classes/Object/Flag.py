##############################################
#	Assignment 3 - Game Programming - HK181
#
#   Group 4:
#   Pham Quang Minh - 1512016
#   Nguyen Dinh Hao - 1510896
#   Vu Anh Tuan - 1513888
############################################

import pygame as pg
from Classes.Constants import FLAG_DIR, BLACK

class Flag(pg.sprite.Sprite):
    def __init__(self, game, pos_x, pos_y, isCheck = False, type = 0):
        self.groups = game.all_sprites, game.flags
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.type = type

        self.isCheck = isCheck # Check flag is touched or not

        self.flag_list = [pg.transform.scale(pg.image.load(FLAG_DIR + "Flag_1.png"), (120, 250)),
                            pg.transform.scale(pg.image.load(FLAG_DIR + "Flag_2.png"), (120, 250)),
                            pg.transform.scale(pg.image.load(FLAG_DIR + "Flag_3.png"), (120, 250))]
                            
        self.image = self.flag_list[type]
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y