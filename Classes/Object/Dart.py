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
from Classes.Constants import ITEM_DIR, BLACK
vec = pg.math.Vector2

class Dart(pg.sprite.Sprite):
    def __init__(self, game, player):
        self.groups = game.all_sprites, game.darts
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.player = player

        self.isRight = self.player.isRight

        self.dart_list = [pg.transform.rotate(pg.image.load(ITEM_DIR + "Dart.png"), 45),
                            pg.transform.rotate(pg.image.load(ITEM_DIR + "Dart.png"), 225)]

        self.image = self.dart_list[0]
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image) # Mask of dart

        self.rect.y = self.player.pos.y - 70
        
        if self.isRight:
            self.rect.x = self.player.pos.x - 15
            self.pos_x = self.player.pos.x - 15

        else:
            self.rect.x = self.player.pos.x - 75
            self.pos_x = self.player.pos.x - 75

    def update(self):
        if self.isRight:
            self.image = self.dart_list[0]
            self.rect.x += 20

            if self.rect.x - self.pos_x > 500:
                self.kill() 

        else:
            self.image = self.dart_list[1]
            self.rect.x -= 20

            if self.pos_x - self.rect.x > 500:
                self.kill() 