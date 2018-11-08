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

class Sound:
    def __init__(self):
        self.bgMusic = pg.mixer.music.load("Music.BG_MUSIC")
        self.hitSound = pg.mixer.Sound("Music.HIT_SOUND")       

    def playBgMusic(self):
        pg.mixer.music.play(0)

    def playHitSound(self):
        self.hitSound.play()

    def stopHitSound(self):
        self.hitSound.stop()