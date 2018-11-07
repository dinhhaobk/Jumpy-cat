##############################################
#	Assignment 3 - Game Programming - HK181
#
#   Group 4:
#   Pham Quang Minh - 1512016
#   Nguyen Dinh Hao - 1510896
#   Vu Anh Tuan - 1513888
############################################

import pygame as pg
from Classes.Constants import CHICKEN_DIR, BLACK
from random import choice

class Chicken(pg.sprite.Sprite):
    def __init__(self, game, pos_x, pos_y):
        self.groups = game.all_sprites, game.chickens
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.speed = choice([4, 5, 6])
        self.time_to_change_dir = choice([4000, 4500, 5000])
        self.isRight = True

        self.current_frame = 0
        self.last_update = 0
        self.last_update2 = 0

        self.chicken_list_r = [pg.transform.scale(pg.image.load(CHICKEN_DIR + "Dragonfly_1.png").convert(), (int(369 * 0.2), int(268 * 0.2))),
                                pg.transform.scale(pg.image.load(CHICKEN_DIR + "Dragonfly_2.png").convert(), (int(362 * 0.2), int(211 * 0.2))),
                                pg.transform.scale(pg.image.load(CHICKEN_DIR + "Dragonfly_3.png").convert(), (int(369 * 0.2), int(266 * 0.2))),
                                pg.transform.scale(pg.image.load(CHICKEN_DIR + "Dragonfly_4.png").convert(), (int(362 * 0.2), int(208 * 0.2)))]

        self.dragonfly_list_l = []
        for img in range(0, len(self.dragonfly_list_r)):
            self.dragonfly_list_l.append(pg.transform.flip(self.dragonfly_list_r[img], True, False))
                            
        self.image = self.dragonfly_list_r[0]

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def update(self):
        now = pg.time.get_ticks() # Count time to change frames
        now2 = pg.time.get_ticks() # Count time to change direction    

        if self.isRight:
            self.rect.x += self.speed
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.dragonfly_list_r)
                    
                self.image = self.dragonfly_list_r[self.current_frame]
         
                if now2 - self.last_update2 > self.time_to_change_dir:
                    self.last_update2 = now2
                    self.isRight = False
        
        else:
            self.rect.x -= self.speed
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.dragonfly_list_l)
                    
                self.image = self.dragonfly_list_l[self.current_frame]
               
                if now2 - self.last_update2 > self.time_to_change_dir:
                    self.last_update2 = now2
                    self.isRight = True