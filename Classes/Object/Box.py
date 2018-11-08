##############################################
#	Assignment 3 - Game Programming - HK181
#
#   Group 4:
#   Pham Quang Minh - 1512016
#   Nguyen Dinh Hao - 1510896
#   Vu Anh Tuan - 1513888
############################################

import pygame as pg
from Classes.Constants import BOX_DIR, BLACK

class Box(pg.sprite.Sprite):
    def __init__(self, game, pos_x, pos_y, type):
        self.groups = game.all_sprites, game.boxs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.type = type

        self.box_list = [pg.transform.scale(pg.image.load(BOX_DIR + "Heart_box.png"), (60, 60)),
                        pg.transform.scale(pg.image.load(BOX_DIR + "Shield_box.png"), (60, 60)),
                        pg.transform.scale(pg.image.load(BOX_DIR + "Dart_box2.png"), (60, 60)),
                        pg.transform.scale(pg.image.load(BOX_DIR + "Random_box.png"), (60, 60))]

        self.image = self.box_list[type - 1]
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y