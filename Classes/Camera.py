##############################################
#	Assignment 3 - Game Programming - HK181
#
#   Group 4:
#   Pham Quang Minh - 1512016
#   Nguyen Dinh Hao - 1510896
#   Vu Anh Tuan - 1513888
############################################

import pygame as pg
from Classes.Constants import WIDTH

def RelRect(actor, camera):
    return pg.Rect(actor.rect.x - camera.rect.x, actor.rect.y - camera.rect.y, actor.rect.w, actor.rect.h)

class Camera(object):
    # Class for center screen on the player
    def __init__(self, screen, player, level_width, level_height):
        self.player = player
        self.rect = screen.get_rect()
        self.rect.center = self.player.rect.center
        self.world_rect = pg.Rect(0, 0, level_width, level_height)

    def update(self):
      if self.player.pos.x > self.rect.centerx + 25:
          self.rect.centerx = self.player.pos.x - 25
      if self.player.pos.x < self.rect.centerx - WIDTH / 2: 
          self.player.pos.x = self.rect.centerx - WIDTH / 2 # Not let cat move left
      if self.player.pos.y > self.rect.centery + 25:
          self.rect.centery = self.player.pos.y - 25
      if self.player.pos.y < self.rect.centery - 25:
          self.rect.centery = self.player.pos.y + 25
      self.rect.clamp_ip(self.world_rect)

    def draw_sprites(self, surf, sprites):
        for s in sprites:
            if s.rect.colliderect(self.rect):
                surf.blit(s.image, RelRect(s, self))