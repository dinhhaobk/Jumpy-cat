##############################################
#	Assignment 3 - Game Programming - HK181
#
#   Group 4:
#   Pham Quang Minh - 1512016
#   Nguyen Dinh Hao - 1510896
#   Vu Anh Tuan - 1513888
############################################

import pygame as pg
from Classes.Object.Coin import Coin
from Classes.Constants import GROUND_DIR, BLACK
from random import choice

class Ground(pg.sprite.Sprite):
    def __init__(self, game, pos_x, pos_y, type = 0, canMoveX = False, canMoveY = False):
        self.groups = game.all_sprites, game.grounds
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.type = type

        self.last_update = 0
        self.canMoveX = canMoveX
        self.canMoveY = canMoveY

        self.ground_list = [pg.transform.scale(pg.image.load(GROUND_DIR + "ground1.png"), (1022, 94)),
                            pg.transform.scale(pg.image.load(GROUND_DIR + "ground2.png"), (511, 47)),
                            pg.transform.scale(pg.image.load(GROUND_DIR + "ground3.png"), (380, 47)),
                            pg.transform.scale(pg.image.load(GROUND_DIR + "ground4.png"), (200, 50))]
                            
        self.image = self.ground_list[type - 1]
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

        self.speed = 2
        self.isMoveRight = True
        self.isMoveDown = False

        # Init coin on ground
        self.number_of_coins = choice([2, 3, 4])
        
        if self.type == 2:
            for coin in range(3):
                Coin(self.game, self.rect.x + coin * 100 + 150, self.rect.y - 50)

        if self.type == 3:
            for coin in range(self.number_of_coins):
                if self.number_of_coins == 2:
                    Coin(self.game, self.rect.x + coin * 100 + 120, self.rect.y - 50)
                elif self.number_of_coins == 3:
                    Coin(self.game, self.rect.x + coin * 100 + 70, self.rect.y - 50)
                elif self.number_of_coins == 4:
                    Coin(self.game, self.rect.x + coin * 100 + 20, self.rect.y - 50)

    def update(self):
        # Ground can move left - right
        if self.canMoveX:
            now = pg.time.get_ticks() # Count time to change direction of moving ground

            if self.isMoveRight:
                self.rect.x += self.speed
                if now - self.last_update > 7500:
                    self.last_update = now
                    self.isMoveRight = False

            else:
                self.rect.x -= self.speed
                if now - self.last_update > 7500:
                    self.last_update = now
                    self.isMoveRight = True

        # Ground can move up - down
        if self.canMoveY:
            now = pg.time.get_ticks() # Count time to change direction of moving ground

            if self.isMoveDown:
                self.rect.y += self.speed
                if now - self.last_update > 4000:
                    self.last_update = now
                    self.isMoveDown = False

            else:
                self.rect.y -= self.speed
                if now - self.last_update > 4000:
                    self.last_update = now
                    self.isMoveDown = True



