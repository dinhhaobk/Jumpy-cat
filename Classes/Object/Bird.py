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
from random import choice

class Bird(pg.sprite.Sprite):
    def __init__(self, game, pos_x, pos_y):
        self.groups = game.all_sprites, game.birds
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.speed = choice([2, 3, 4])
        self.time_to_change_dir = choice([3000, 3500, 4000])
        self.isRight = True

        self.current_frame = 0
        self.last_update = 0
        self.last_update2 = 0

        self.bird_list_r = [pg.transform.scale(pg.image.load(BIRD_DIR + "Bird_1.png"), (int(146 * 0.65), int(143 * 0.65))),
                            pg.transform.scale(pg.image.load(BIRD_DIR + "Bird_2.png"), (int(146 * 0.65), int(141 * 0.65))),
                            pg.transform.scale(pg.image.load(BIRD_DIR + "Bird_3.png"), (int(146 * 0.65), int(130 * 0.65))),
                            pg.transform.scale(pg.image.load(BIRD_DIR + "Bird_4.png"), (int(171 * 0.65), int(122 * 0.65))),
                            pg.transform.scale(pg.image.load(BIRD_DIR + "Bird_5.png"), (int(182 * 0.65), int(88 * 0.65))),
                            pg.transform.scale(pg.image.load(BIRD_DIR + "Bird_6.png"), (int(146 * 0.65), int(118 * 0.65))),
                            pg.transform.scale(pg.image.load(BIRD_DIR + "Bird_7.png"), (int(146 * 0.65), int(124 * 0.65))),
                            pg.transform.scale(pg.image.load(BIRD_DIR + "Bird_8.png"), (int(146 * 0.65), int(120 * 0.65))),
                            pg.transform.scale(pg.image.load(BIRD_DIR + "Bird_9.png"), (int(146 * 0.65), int(109 * 0.65))),
                            pg.transform.scale(pg.image.load(BIRD_DIR + "Bird_10.png"), (int(146 * 0.65), int(110 * 0.65))),
                            pg.transform.scale(pg.image.load(BIRD_DIR + "Bird_11.png"), (int(146 * 0.65), int(108 * 0.65))),
                            pg.transform.scale(pg.image.load(BIRD_DIR + "Bird_12.png"), (int(146 * 0.65), int(106 * 0.65))),
                            pg.transform.scale(pg.image.load(BIRD_DIR + "Bird_13.png"), (int(168 * 0.65), int(88 * 0.65))),
                            pg.transform.scale(pg.image.load(BIRD_DIR + "Bird_14.png"), (int(180 * 0.65), int(114 * 0.65)))]

        self.bird_list_l = []
        for img in range(0, len(self.bird_list_r)):
            self.bird_list_l.append(pg.transform.flip(self.bird_list_r[img], True, False))
                            
        self.image = self.bird_list_r[0]

        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image) # Mask of bird
        self.rect.x = pos_x
        self.rect.y = pos_y

    def update(self):
        now = pg.time.get_ticks() # Count time to change frames
        now2 = pg.time.get_ticks() # Count time to change direction

        if self.isRight:
            self.rect.x += self.speed
            if now - self.last_update > 70:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.bird_list_r)
                    
                self.image = self.bird_list_r[self.current_frame]
          
                if now2 - self.last_update2 > self.time_to_change_dir:
                    self.last_update2 = now2
                    self.isRight = False
        
        else:
            self.rect.x -= self.speed
            if now - self.last_update > 70:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.bird_list_l)
                    
                self.image = self.bird_list_l[self.current_frame]
               
                if now2 - self.last_update2 > self.time_to_change_dir:
                    self.last_update2 = now2
                    self.isRight = True

