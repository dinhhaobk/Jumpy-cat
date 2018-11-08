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
        self.bgMusic = pg.mixer.music.load(SOUND_DIR + "bg_music.ogg")
        self.introMusic = pg.mixer.music.load(SOUND_DIR + "intro_music.ogg")

        self.jumpSound = pg.mixer.Sound(SOUND_DIR + "jump.wav")
        self.coinSound = pg.mixer.Sound(SOUND_DIR + "coin.wav")   
        self.chickenSound = pg.mixer.Sound(SOUND_DIR + "chicken.wav")  
        self.birdSound = pg.mixer.Sound(SOUND_DIR + "bird.wav")  

    def playBgMusic(self):
        self.bgMusic = pg.mixer.music.load(SOUND_DIR + "bg_music.ogg")
        pg.mixer.music.play(-1)

    def playIntroMusic(self):
        self.introMusic = pg.mixer.music.load(SOUND_DIR + "intro_music.ogg")
        pg.mixer.music.play(-1)

    def musicFadeOut(self):
        pg.mixer.music.fadeout(500)

    def playJumpSound(self):
        self.jumpSound.stop()
        self.jumpSound.play()

    def playCoinSound(self):
        self.coinSound.stop()
        self.coinSound.play()

    def playChickenSound(self):
        self.chickenSound.stop()
        self.chickenSound.play()

    def playBirdSound(self):
        self.birdSound.stop()
        self.birdSound.play()
        