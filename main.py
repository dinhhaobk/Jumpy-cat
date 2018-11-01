##############################################
#	Assignment 3 - Game Programming - HK181
#
#   Group 4:
#   Pham Quang Minh - 1512016
#   Nguyen Dinh Hao - 1510896
#   Vu Anh Tuan - 1513888
############################################

import pygame as pg
import random
from Classes.Constants import *
from Classes.Spritesheet import Spritesheet
from Classes.Player import *
from Classes.Ground import *
from Classes.Cloud import *
from Classes.Items import *
from Classes.Bird import *

class Game:
    def __init__(self):
        # Init game window, title, clock, font, data
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(FULL_TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()

    # Load all data
    def load_data(self):
        # Read highscore file
        with open(HIGHSCORE_FILE, 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0

        # Load spritesheet image
        self.spritesheet = Spritesheet(SPRITESHEET_FILE)

        # Load sounds
        self.jump_sound = pg.mixer.Sound("./Resources/Sound/jump1.wav")
        self.boost_sound = pg.mixer.Sound("./Resources/Sound/boost.wav")    

    # Start a new game
    def start(self):   
        self.score = 0
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.grounds = pg.sprite.Group() # Group of ground sprites
        self.player = Player(self) 
        
        for ground in GROUND_LIST:
            Ground(self, *ground, 3)
        
        self.bg_music = pg.mixer.music.load("./Resources/Sound/bg_music.ogg")
        self.run()

    # Run a loop game
    def run(self):   
        pg.mixer.music.play(loops = -1)
        self.playing = True

        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        pg.mixer.music.fadeout(500)

    # Game loop - events
    def events(self):
        for event in pg.event.get():
            # Check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    self.player.jump_cut()

    # Game loop - update
    def update(self):
        # Game Loop - Update
        self.all_sprites.update()

        # Check if player hits a ground - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.grounds, False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                if self.player.pos.x < lowest.rect.right + 10 and \
                   self.player.pos.x > lowest.rect.left - 10:
                    if self.player.pos.y < lowest.rect.centery:
                        self.player.pos.y = lowest.rect.top
                        self.player.vel.y = 0
                        self.player.isJump = False

    # Game loop - draw
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 22, WHITE, WIDTH / 2, 15)
        pg.display.flip()

    # Start screen
    def start_game_screen(self): 
        pg.mixer.music.load("./Resources/Sound/intro_music.ogg")
        pg.mixer.music.play(loops = -1)

        self.screen.fill(BGCOLOR)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Arrows to move, Space to jump", 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press a key to play", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        self.draw_text("High Score: " + str(self.highscore), 22, WHITE, WIDTH / 2, 15)
        pg.display.flip()
        self.wait_for_key()
        pg.mixer.music.fadeout(500)

    # Game over screen
    def game_over_screen(self):   
        if not self.running:
            return
        pg.mixer.music.load("./Resources/Sound/intro_music.ogg")
        pg.mixer.music.play(loops = -1)

        self.screen.fill(BGCOLOR)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press a key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)

        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("NEW HIGH SCORE!", 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)

            # Write new highscore to file
            with open(HIGHSCORE_FILE) as f:
                f.write(str(self.score)) 
        else:
            self.draw_text("High Score: " + str(self.highscore), 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
        pg.display.flip()
        self.wait_for_key()
        pg.mixer.music.fadeout(500)

    # Waiting key events
    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    # Draw text
    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


###########################################################################
# Init the game
pg.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
pg.init()

myGame = Game()
myGame.start_game_screen()
while myGame.running:
    myGame.start()
    myGame.game_over_screen()

pg.quit()