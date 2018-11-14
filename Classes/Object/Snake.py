##############################################
#	Assignment 3 - Game Programming - HK181
#
#   Group 4:
#   Pham Quang Minh - 1512016
#   Nguyen Dinh Hao - 1510896
#   Vu Anh Tuan - 1513888
############################################

import pygame as pg
from Classes.Constants import SNAKE_DIR
from random import choice
vec = pg.math.Vector2

class Snake(pg.sprite.Sprite):
    def __init__(self, game, player, pos_x, pos_y):
        self.groups = game.all_sprites, game.snakes
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.player = player
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.life = 5
        self.speed = 2
        self.pos_to_change_dir = choice([100, 150, 200, 250])
        self.isRight = True

        self.isIdle = True
        self.isAttack = False
        self.isDie = False

        self.current_frame = 0
        self.last_update = 0

        self.load_images()
        self.image = self.idle_frame_r[0]

        self.rect = self.image.get_rect()
        #self.mask = pg.mask.from_surface(self.image) # Mask of snake
        self.rect.x = pos_x
        self.rect.y = pos_y

        self.pos = vec(self.rect.x, self.rect.y) # Position of snake
        self.movx = 0
        self.movy = 5

    def load_images(self):
        # Idle state
        self.idle_frame_l = [pg.image.load(SNAKE_DIR + "Idle (1).png"), pg.image.load(SNAKE_DIR + "Idle (2).png"),
                            pg.image.load(SNAKE_DIR + "Idle (3).png"), pg.image.load(SNAKE_DIR + "Idle (4).png"),
                            pg.image.load(SNAKE_DIR + "Idle (5).png"), pg.image.load(SNAKE_DIR + "Idle (6).png"),
                            pg.image.load(SNAKE_DIR + "Idle (7).png"), pg.image.load(SNAKE_DIR + "Idle (8).png"),
                            pg.image.load(SNAKE_DIR + "Idle (9).png"), pg.image.load(SNAKE_DIR + "Idle (10).png"),
                            pg.image.load(SNAKE_DIR + "Idle (11).png"), pg.image.load(SNAKE_DIR + "Idle (12).png"),
                            pg.image.load(SNAKE_DIR + "Idle (13).png"), pg.image.load(SNAKE_DIR + "Idle (14).png"),
                            pg.image.load(SNAKE_DIR + "Idle (15).png"), pg.image.load(SNAKE_DIR + "Idle (16).png")]
        self.idle_frame_r = []
        for img in range(0, len(self.idle_frame_l)):
            self.idle_frame_r.append(pg.transform.flip(self.idle_frame_l[img], True, False))

        # Attack state
        self.attack_frame_l = [pg.image.load(SNAKE_DIR + "Attack (1).png"), pg.image.load(SNAKE_DIR + "Attack (2).png"),
                            pg.image.load(SNAKE_DIR + "Attack (3).png"), pg.image.load(SNAKE_DIR + "Attack (4).png"),
                            pg.image.load(SNAKE_DIR + "Attack (5).png"), pg.image.load(SNAKE_DIR + "Attack (6).png")]
        self.attack_frame_r = []
        for img in range(0, len(self.attack_frame_l)):
            self.attack_frame_r.append(pg.transform.flip(self.attack_frame_l[img], True, False))

        # Shoot state
        self.shoot_frame_l = [pg.image.load(SNAKE_DIR + "Shoot (1).png"), pg.image.load(SNAKE_DIR + "Shoot (2).png"),
                            pg.image.load(SNAKE_DIR + "Shoot (3).png"), pg.image.load(SNAKE_DIR + "Shoot (4).png"),
                            pg.image.load(SNAKE_DIR + "Shoot (5).png"), pg.image.load(SNAKE_DIR + "Shoot (6).png"),
                            pg.image.load(SNAKE_DIR + "Shoot (7).png"), pg.image.load(SNAKE_DIR + "Shoot (8).png"),
                            pg.image.load(SNAKE_DIR + "Shoot (9).png")]
        self.shoot_frame_r = []
        for img in range(0, len(self.shoot_frame_l)):
            self.shoot_frame_r.append(pg.transform.flip(self.shoot_frame_l[img], True, False))

        # Die state
        self.die_frame_l = [pg.image.load(SNAKE_DIR + "Die (1).png"), pg.image.load(SNAKE_DIR + "Die (2).png"),
                            pg.image.load(SNAKE_DIR + "Die (3).png"), pg.image.load(SNAKE_DIR + "Die (4).png"),
                            pg.image.load(SNAKE_DIR + "Die (5).png"), pg.image.load(SNAKE_DIR + "Die (6).png"),
                            pg.image.load(SNAKE_DIR + "Die (7).png"), pg.image.load(SNAKE_DIR + "Die (8).png")]
        self.die_frame_r = []
        for img in range(0, len(self.die_frame_l)):
            self.die_frame_r.append(pg.transform.flip(self.die_frame_l[img], True, False))


    def update(self):

        if (abs(self.pos.x - self.player.pos.x) > 600) or (self.pos.y - self.player.pos.y > 100):
            self.isIdle = True
            self.isAttack = False
            self.animate_idle()
        else:
            if (self.pos.x > self.player.pos.x and (not self.isRight)) or (self.pos.x < self.player.pos.x and (self.isRight)):
                    self.isIdle = False
                    self.isAttack = True
                    self.animate_attack()
            else:
                self.isIdle = True
                self.isAttack = False
                self.animate_idle()

    def animate_idle(self):
        now = pg.time.get_ticks() # Count time to change frames

        # Idle animation
        if self.isIdle and not self.isAttack:
            if self.isRight:
                self.pos.x += self.speed 
                if now - self.last_update > 60:
                    self.last_update = now
                    self.current_frame = (self.current_frame + 1) % len(self.idle_frame_r)
                        
                    self.image = self.idle_frame_r[self.current_frame]
            
                    if self.pos.x - self.pos_x > self.pos_to_change_dir:
                        self.isRight = False
            
            else:
                self.pos.x -= self.speed
                if now - self.last_update > 60:
                    self.last_update = now
                    self.current_frame = (self.current_frame + 1) % len(self.idle_frame_l)
                        
                    self.image = self.idle_frame_l[self.current_frame]
                
                    if self.pos_x - self.pos.x > self.pos_to_change_dir:
                        self.isRight = True

            self.rect.center = self.pos

    def animate_attack(self):
        now = pg.time.get_ticks() # Count time to change frames
            
        # Attack animation
        if self.isAttack and not self.isIdle:
            if self.isRight:
                self.pos.x += self.speed * 4
                if now - self.last_update > 80:
                    self.last_update = now
                    self.current_frame = (self.current_frame + 1) % len(self.attack_frame_r)
                        
                    self.image = self.attack_frame_r[self.current_frame]
                    self.rect = self.image.get_rect()
            
                    if self.pos.x < self.player.pos.x:
                        self.isAttack = False
                        self.pos_to_change_dir = choice([100, 150, 200])
                
                self.rect.x = self.pos.x - 120
                self.rect.y = self.pos.y - 40
            
            else:
                self.pos.x -= self.speed * 4
                if now - self.last_update > 80:
                    self.last_update = now
                    self.current_frame = (self.current_frame + 1) % len(self.attack_frame_l)
                        
                    self.image = self.attack_frame_l[self.current_frame]
                
                    if self.pos.x > self.player.pos.x:
                        self.isAttack = False
                        self.pos_to_change_dir = choice([100, 150, 200])

                self.rect.x = self.pos.x
                self.rect.y = self.pos.y - 40