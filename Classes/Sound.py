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

        self.arrowSound = pg.mixer.Sound(SOUND_DIR + "arrow.ogg")
        self.chooseSound = pg.mixer.Sound(SOUND_DIR + "choose.ogg")

        self.jumpSound = pg.mixer.Sound(SOUND_DIR + "jump.wav")
        self.coinSound = pg.mixer.Sound(SOUND_DIR + "coin.wav") 
        self.dartSound = pg.mixer.Sound(SOUND_DIR + "dart.wav")  
        self.flagSound = pg.mixer.Sound(SOUND_DIR + "flag.wav")   
        self.itemSound = pg.mixer.Sound(SOUND_DIR + "item.wav")
        self.hurtSound = pg.mixer.Sound(SOUND_DIR + "hurt.wav")

        self.dragonflySound = pg.mixer.Sound(SOUND_DIR + "dragonfly.wav")  
        self.chickenSound = pg.mixer.Sound(SOUND_DIR + "chicken.wav")  
        self.birdSound = pg.mixer.Sound(SOUND_DIR + "bird.wav")  
        self.snakeSound = pg.mixer.Sound(SOUND_DIR + "snake.ogg")

        self.dartHitSnakeSound = pg.mixer.Sound(SOUND_DIR + "dart_hit_snake.ogg")

    def playBgMusic(self):
        self.bgMusic = pg.mixer.music.load(SOUND_DIR + "bg_music.ogg")
        pg.mixer.music.play(-1)

    def playIntroMusic(self):
        self.introMusic = pg.mixer.music.load(SOUND_DIR + "intro_music.ogg")
        pg.mixer.music.play(-1)

    def musicFadeOut(self):
        pg.mixer.music.fadeout(500)

    def playArrowSound(self):
        self.arrowSound.stop()
        self.arrowSound.play()

    def playChooseSound(self):
        self.chooseSound.stop()
        self.chooseSound.play()
        
    def playJumpSound(self):
        self.jumpSound.stop()
        self.jumpSound.play()

    def playCoinSound(self):
        self.coinSound.stop()
        self.coinSound.play()

    def playDartSound(self):
        self.dartSound.stop()
        self.dartSound.play()

    def playFlagSound(self):
        self.flagSound.stop()
        self.flagSound.play()

    def playItemSound(self):
        self.itemSound.stop()
        self.itemSound.play()

    def playHurtSound(self):
        self.hurtSound.stop()
        self.hurtSound.play()

    def playDragonflySound(self):
        self.dragonflySound.stop()
        self.dragonflySound.play()

    def playChickenSound(self):
        self.chickenSound.stop()
        self.chickenSound.play()

    def playBirdSound(self):
        self.birdSound.stop()
        self.birdSound.play()

    def playSnakeSound(self):
        self.snakeSound.stop()
        self.snakeSound.play()
        
    def playDartHitSnakeSound(self):
        self.dartHitSnakeSound.stop()
        self.dartHitSnakeSound.play()