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
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.life = 3 # Number of lives
        self.dart = 2 # Number of darts
        self.isShield = False # Item shield from box
        self.image_shield = pg.image.load(ITEM_DIR + "Shield.png") # Image of shield

        self.checkPoint = FLAG_LIST[0]
        if self.game.optionCharacter == 1:
            self.character = CAT_DIR
        else:
            self.character = CAT_DIR_2

        self.isWalk = False
        self.isJump = False
        self.isRight = True

        self.current_frame = 0
        self.last_update = 0

        self.checkJumpAni = False
        self.checkFallAni = False
        self.checkHurtAni = False

        self.load_images()
        self.image = self.idle_frames_r[0]
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image) # Mask of player

        self.rect.center = (50, MAP_HEIGHT - 60)
        self.pos = vec(50, MAP_HEIGHT - 60) # Position of player
        self.vel = vec(0, 0) # Velocity of player
        self.acc = vec(0, 0) # Acceleration of player

    # Load all images of cat
    def load_images(self):
        # Idle state
        self.idle_img_list = ["Idle (1).png", "Idle (2).png", "Idle (3).png", "Idle (4).png", 
                                "Idle (5).png", "Idle (6).png", "Idle (7).png", "Idle (8).png", 
                                "Idle (9).png", "Idle (10).png"]
        self.idle_frames_r = []
        self.idle_frames_l = []

        for img in range(0, len(self.idle_img_list)):
            self.idle_frames_r.append(pg.image.load(self.character + self.idle_img_list[img]))

        for frame in range(0, len(self.idle_frames_r)):
            self.idle_frames_r[frame] = pg.transform.scale(self.idle_frames_r[frame], (PLAYER_SCALE[0], PLAYER_SCALE[1]))
            self.idle_frames_r[frame].set_colorkey(BLACK)
            self.idle_frames_l.append(pg.transform.flip(self.idle_frames_r[frame], True, False))

        # Walk state
        self.walk_img_list = ["Walk (1).png", "Walk (2).png", "Walk (3).png", "Walk (4).png", 
                                "Walk (5).png", "Walk (6).png", "Walk (7).png", "Walk (8).png", 
                                "Walk (9).png", "Walk (10).png"]
        self.walk_frames_r = []
        self.walk_frames_l = []

        for img in range(0, len(self.walk_img_list)):
            self.walk_frames_r.append(pg.image.load(self.character + self.walk_img_list[img]))

        for frame in range(0, len(self.walk_frames_r)):
            self.walk_frames_r[frame] = pg.transform.scale(self.walk_frames_r[frame], (PLAYER_SCALE[0], PLAYER_SCALE[1]))
            self.walk_frames_r[frame].set_colorkey(BLACK)
            self.walk_frames_l.append(pg.transform.flip(self.walk_frames_r[frame], True, False))

        # Jump state
        self.jump_img_list = ["Jump (1).png", "Jump (2).png", "Jump (3).png","Jump (4).png", 
                                "Jump (5).png", "Jump (6).png", "Jump (7).png", "Jump (8).png"]
        self.jump_frames_r = []
        self.jump_frames_l = []

        for img in range(0, len(self.jump_img_list)):
            self.jump_frames_r.append(pg.image.load(self.character + self.jump_img_list[img]))

        for frame in range(0, len(self.jump_frames_r)):
            self.jump_frames_r[frame] = pg.transform.scale(self.jump_frames_r[frame], (PLAYER_SCALE[0], PLAYER_SCALE[1]))
            self.jump_frames_r[frame].set_colorkey(BLACK)
            self.jump_frames_l.append(pg.transform.flip(self.jump_frames_r[frame], True, False))

        # Fall state
        self.fall_img_list = ["Fall (1).png", "Fall (2).png", "Fall (3).png", "Fall (4).png", 
                                "Fall (5).png", "Fall (6).png", "Fall (7).png", "Fall (8).png",]
        self.fall_frames_r = []
        self.fall_frames_l = []

        for img in range(0, len(self.fall_img_list)):
            self.fall_frames_r.append(pg.image.load(self.character + self.fall_img_list[img]))

        for frame in range(0, len(self.fall_frames_r)):
            self.fall_frames_r[frame] = pg.transform.scale(self.fall_frames_r[frame], (PLAYER_SCALE[0], PLAYER_SCALE[1]))
            self.fall_frames_r[frame].set_colorkey(BLACK)
            self.fall_frames_l.append(pg.transform.flip(self.fall_frames_r[frame], True, False))

        ### Hurt state
        # self.hurt_img_list = ["Hurt (1).png", "Hurt (2).png", "Hurt (3).png", "Hurt (4).png",
        #                         "Hurt (5).png", "Hurt (6).png", "Hurt (7).png", "Hurt (8).png",
        #                         "Hurt (9).png", "Hurt (10).png"]
        # self.hurt_frames_r = []
        # self.hurt_frames_l = []

        # for img in range(0, len(self.hurt_img_list)):
        #     self.hurt_frames_r.append(pg.image.load(self.character + self.hurt_img_list[img]))

        # for frame in range(0, len(self.hurt_frames_r)):
        #     if frame == 0:
        #         self.hurt_frames_r[frame] = pg.transform.scale(self.hurt_frames_r[frame], (335 // 5, 380 // 5))
        #     elif frame == 1:
        #         self.hurt_frames_r[frame] = pg.transform.scale(self.hurt_frames_r[frame], (324 // 5, 410 // 5))
        #     elif frame == 2:
        #         self.hurt_frames_r[frame] = pg.transform.scale(self.hurt_frames_r[frame], (345 // 5, 437 // 5))
        #     elif frame == 3:
        #         self.hurt_frames_r[frame] = pg.transform.scale(self.hurt_frames_r[frame], (373 // 5, 418 // 5))
        #     elif frame == 4:
        #         self.hurt_frames_r[frame] = pg.transform.scale(self.hurt_frames_r[frame], (356 // 5, 353 // 5))
        #     elif frame == 5:
        #         self.hurt_frames_r[frame] = pg.transform.scale(self.hurt_frames_r[frame], (351 // 5, 340 // 5))
        #     elif frame == 6:
        #         self.hurt_frames_r[frame] = pg.transform.scale(self.hurt_frames_r[frame], (356 // 5, 331 // 5))
        #     elif frame == 7:
        #         self.hurt_frames_r[frame] = pg.transform.scale(self.hurt_frames_r[frame], (341 // 5, 380 // 5))
        #     elif frame == 8:
        #         self.hurt_frames_r[frame] = pg.transform.scale(self.hurt_frames_r[frame], (351 // 5, 420 // 5))
        #     elif frame == 9:
        #         self.hurt_frames_r[frame] = pg.transform.scale(self.hurt_frames_r[frame], (337 // 5, 427 // 5))
        #     self.hurt_frames_r[frame].set_colorkey(BLACK)
        #     self.hurt_frames_l.append(pg.transform.flip(self.hurt_frames_r[frame], True, False))

        ### Dead state
        # self.dead_img_list = ["Dead (1).png", "Dead (2).png", "Dead (3).png", "Dead (4).png", 
        #                         "Dead (5).png", "Dead (6).png", "Dead (7).png", "Dead (8).png", 
        #                         "Dead (9).png", "Dead (10).png"]
        # self.dead_frames_r = []
        # self.dead_frames_l = []

        # for img in range(0, len(self.dead_img_list) - 1):
        #     self.dead_frames_r.append(pg.image.load(self.character + self.dead_img_list[img]))

        # for frame in range(0, len(self.dead_frames_r) - 1):
        #     self.dead_frames_r[frame] = pg.transform.scale(self.dead_frames_r[frame], (PLAYER_SCALE[0], PLAYER_SCALE[1]))
        #     self.dead_frames_r[frame].set_colorkey(BLACK)
        #     self.dead_frames_l.append(pg.transform.flip(self.dead_frames_r[frame], True, False))

    # Handle when cat jumps
    def jump(self):
        # Jump only if standing on a ground
        self.rect.y += 2
        hits = pg.sprite.spritecollide(self, self.game.grounds, False)
        self.rect.y -= 2
        if hits and not self.isJump:
            self.isJump = True
            self.vel.y = -PLAYER_JUMP
            self.game.sound.playJumpSound()

        if self.isJump:
            self.animate_jump() # Animation for jump

    # Handle when cat jumps 1 bit SCREEN_HEIGHT
    def jump_cut(self):
        if self.isJump:
            if self.vel.y < -3:
                self.vel.y = -3

            self.animate_fall() # Animation for fall

    # Handle postion of cat
    def update(self):
        self.animate()
        self.acc = vec(0, PLAYER_GRAV)

        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.isRight = False
            self.acc.x = -PLAYER_ACC

        if keys[pg.K_RIGHT]:
            self.isRight = True
            self.acc.x = PLAYER_ACC

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

        # If player collect shield
        if self.isShield:
            if self.isRight:
                #self.image.fill((255,255,255,0))
                #self.image = img
                self.image.blit(self.image_shield, (20, 55))
            else:
                #self.image.fill((255,255,255,0))
                #self.image = self.current_frame
                self.image.blit(self.image_shield, (15, 55))

    # Handle animation of cat
    def animate(self):
        now = pg.time.get_ticks()

        if self.vel.x != 0:
            self.isWalk = True
        else:
            self.isWalk = False

        # Idle animation
        if not self.isJump and not self.isWalk:
            if self.isRight:
                self.image = self.idle_frames_r[(self.current_frame + 1) % len(self.idle_frames_r)]
                if now - self.last_update > 80:
                    self.last_update = now
                    self.current_frame = (self.current_frame + 1) % len(self.idle_frames_r)

                    bottom = self.rect.bottom
                    
                    self.image = self.idle_frames_r[self.current_frame]

                    self.rect = self.image.get_rect()
                    self.rect.bottom = bottom

            else:
                self.image = self.idle_frames_l[(self.current_frame + 1) % len(self.idle_frames_l)]
                if now - self.last_update > 80:
                    self.last_update = now
                    self.current_frame = (self.current_frame + 1) % len(self.idle_frames_l)

                    bottom = self.rect.bottom
                    
                    self.image = self.idle_frames_l[self.current_frame]

                    self.rect = self.image.get_rect()
                    self.rect.bottom = bottom

        # Walk animation
        if self.isWalk and not self.isJump:
            if self.isRight:
                self.image = self.walk_frames_r[(self.current_frame + 1) % len(self.walk_frames_r)]
                if now - self.last_update > 60:
                    self.last_update = now
                    self.current_frame = (self.current_frame + 1) % len(self.walk_frames_r)

                    bottom = self.rect.bottom

                    self.image = self.walk_frames_r[self.current_frame]

                    self.rect = self.image.get_rect()
                    self.rect.bottom = bottom

            else:
                self.image = self.walk_frames_l[(self.current_frame + 1) % len(self.walk_frames_l)]
                if now - self.last_update > 60:
                    self.last_update = now
                    self.current_frame = (self.current_frame + 1) % len(self.walk_frames_l)

                    bottom = self.rect.bottom

                    self.image = self.walk_frames_l[self.current_frame]

                    self.rect = self.image.get_rect()
                    self.rect.bottom = bottom

        ### Hurt animation
        # if self.isHurt:
        #     if self.isRight:
        #         if not self.checkHurtAni:
        #             self.current_frame = 0
        #             self.image = self.hurt_frames_r[0]
        #             self.checkHurtAni = True

        #         if now - self.last_update_hurt > 100:
        #             self.last_update_hurt = now

        #             if self.current_frame < len(self.hurt_frames_r) - 1:
        #                 self.current_frame = (self.current_frame + 1) % len(self.hurt_frames_r)
        #             else:
        #                 self.isHurt = False
        #                 #self.checkHurtAni = False

        #             bottom = self.rect.bottom

        #             self.image = self.hurt_frames_r[self.current_frame]

        #             self.rect = self.image.get_rect()
        #             self.rect.bottom = bottom

        #     else:
        #         if not self.checkHurtAni:
        #             self.current_frame = 0
        #             self.image = self.hurt_frames_l[0]
        #             self.checkHurtAni = True

        #         if now - self.last_update_hurt > 100:
        #             self.last_update_hurt = now

        #             if self.current_frame < len(self.hurt_frames_l) - 1:
        #                 self.current_frame = (self.current_frame + 1) % len(self.hurt_frames_l)
        #             else:
        #                 self.isHurt = False
        #                 #self.checkHurtAni = False

        #             bottom = self.rect.bottom

        #             self.image = self.hurt_frames_l[self.current_frame]

        #             self.rect = self.image.get_rect()
        #             self.rect.bottom = bottom

        ### Set time for immortal
        # if self.isImmortal:
        #     if now - self.last_update_immortal > 3000:
        #         self.last_update_immortal = now
        #         self.isImmortal = False

        #     else:
        #         self.image.map_rgb(BLACK)


    # Handle jump animation
    def animate_jump(self):
        now = pg.time.get_ticks()

        # Jump animation
        if self.isRight:
            if not self.checkJumpAni:
                self.current_frame = 0
                self.image = self.jump_frames_r[0]
                self.checkJumpAni = True

            if now - self.last_update > 20:
                self.last_update = now

                if self.current_frame < len(self.jump_frames_r) - 1:
                    self.current_frame = (self.current_frame + 1) % len(self.jump_frames_r)

                bottom = self.rect.bottom

                self.image = self.jump_frames_r[self.current_frame]

                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

        else:
            if not self.checkJumpAni:
                self.current_frame = 0
                self.image = self.jump_frames_l[0]
                self.checkJumpAni = True

            self.image = self.jump_frames_l[(self.current_frame + 1) % len(self.jump_frames_l)]
            if now - self.last_update > 20:
                self.last_update = now

                if self.current_frame < len(self.jump_frames_l) - 1:
                    self.current_frame = (self.current_frame + 1) % len(self.jump_frames_l)

                bottom = self.rect.bottom

                self.image = self.jump_frames_l[self.current_frame]

                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

    # Handle fall animation
    def animate_fall(self):
        now = pg.time.get_ticks()

        # Fall animation
        if self.isRight:
            if not self.checkFallAni:
                self.current_frame = 0
                self.image = self.fall_frames_r[0]
                self.checkFallAni = True

            if now - self.last_update > 20:
                self.last_update = now

                if self.current_frame < len(self.fall_frames_r) - 1:
                    self.current_frame = (self.current_frame + 1) % len(self.fall_frames_r)

                bottom = self.rect.bottom

                self.image = self.fall_frames_r[self.current_frame]

                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

        else:
            if not self.checkFallAni:
                self.current_frame = 0
                self.image = self.fall_frames_l[0]
                self.checkFallAni = True

            if now - self.last_update > 20:
                self.last_update = now

                if self.current_frame < len(self.fall_frames_l) - 1:
                    self.current_frame = (self.current_frame + 1) % len(self.fall_frames_l)

                bottom = self.rect.bottom

                self.image = self.fall_frames_l[self.current_frame]

                self.rect = self.image.get_rect()
                self.rect.bottom = bottom