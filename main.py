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
from Classes.Camera import Camera
from Classes.Object.Player import Player
from Classes.Object.Ground import Ground
from Classes.Object.Cloud import Cloud
from Classes.Object.Coin import Coin
from Classes.Object.Dragonfly import Dragonfly
from Classes.Object.Bird import Bird

class Game:
    def __init__(self):
        # Init game window, title, clock, font, data
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        pg.display.set_caption(FULL_TITLE)
        pg.mouse.set_visible(False)
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

        # Load sounds
        self.jump_sound = pg.mixer.Sound("./Resources/Sound/jump1.wav")
        self.boost_sound = pg.mixer.Sound("./Resources/Sound/boost.wav")    

    # Start a new game
    def start(self):   
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.grounds = pg.sprite.Group() # Group of ground sprites
        self.clouds = pg.sprite.Group() # Group of cloud sprites
        self.coins = pg.sprite.Group() # Group of coin sprites    
        self.dragonflys = pg.sprite.Group() # Group of dragonfly sprites 
        self.birds = pg.sprite.Group() # Group of bird sprites
        
        # Init ground
        for ground2 in GROUND_LIST_TYPE1:
            Ground(self, *ground2, 1)
        for ground in GROUND_LIST_TYPE2:
            Ground(self, *ground, 2)     
        for ground3 in GROUND_LIST_TYPE3:
            Ground(self, *ground3, 3)
        for ground4 in GROUND_LIST_TYPE4:
            Ground(self, *ground4, 4) 

        # Init cloud
        for cloud in range(CLOUD_NUMBER):
            Cloud(self, cloud)     
        
        # Init coin
        for coin in COIN_LIST:
            Coin(self, *coin)

        # Init dragonfly
        for dragonfly in DRAGONFLY_LIST:
            Dragonfly(self, *dragonfly)

        # Init bird
        for bird in BIRD_LIST:
            Bird(self, *bird)


        # Init player
        self.player = Player(self) 
        self.camera = Camera(self.screen, self.player, MAP_WIDTH, MAP_HEIGHT) # Init camera
        

        self.score = 0
        self.isPause = False     
        self.bg_music = pg.mixer.music.load("./Resources/Sound/bg_music.ogg")
        self.run()

    # Run a loop game
    def run(self):   
        pg.mixer.music.play(loops = -1)
        self.playing = True

        while self.playing:
            if self.isPause:
                pg.time.wait(100) # Pause game
                self.events()
            else:
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
                if event.key == pg.K_ESCAPE:
                    if self.playing:
                        self.playing = False
                    self.running = False

                if event.key == pg.K_SPACE:
                    if not self.isPause:
                        self.player.jump()

                if event.key == pg.K_p:
                    if self.isPause:
                        self.isPause = False
                    else:
                        self.isPause = True
                        
            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    if not self.isPause:
                        self.player.jump_cut()

    # Game loop - update
    def update(self):
        # Update all sprites and camera
        self.all_sprites.update()
        self.camera.update()

        # Check if player hits a ground - only if falling
        if self.player.vel.y > 0:
            ground_hit_list = pg.sprite.spritecollide(self.player, self.grounds, False)
            if len(ground_hit_list) == 1:
                lowest = ground_hit_list[0]
                # for hit in hits:
                #     if hit.rect.bottom > lowest.rect.bottom:
                #         lowest = hit
                if (self.player.pos.x < lowest.rect.right + 10) and (self.player.pos.x > lowest.rect.left - 10):
                    if self.player.pos.y < lowest.rect.centery:
                        self.player.pos.y = lowest.rect.top
                        self.player.vel.y = 0
                        self.player.isJump = self.player.checkJumpAni = self.player.checkFallAni = False
            
            elif len(ground_hit_list) == 2:
                low1 = ground_hit_list[0]
                low2 = ground_hit_list[1]
                if low1.rect.top == low2.rect.top:
                    if (self.player.pos.x < low1.rect.right + 10) and (self.player.pos.x > low1.rect.left - 10):
                        if self.player.pos.y < low1.rect.centery:
                            self.player.pos.y = low1.rect.top
                            self.player.vel.y = 0
                            self.player.isJump = self.player.checkJumpAni = self.player.checkFallAni = False

                    elif (self.player.pos.x < low2.rect.right + 10) and (self.player.pos.x > low2.rect.left - 10):
                        if self.player.pos.y < low2.rect.centery:
                            self.player.pos.y = low2.rect.top
                            self.player.vel.y = 0
                            self.player.isJump = self.player.checkJumpAni = self.player.checkFallAni = False
        
        # Check if player hits a coin - if yes then + score
        coin_list = pg.sprite.spritecollide(self.player, self.coins, False)
        for i in range(len(coin_list)):
            coin_list[i - 1].kill()
            self.score += 50

    # Game loop - draw
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.camera.draw_sprites(self.screen, self.all_sprites)
        self.draw_text(str(self.score), 36, WHITE, SCREEN_WIDTH / 2, 36)
        self.draw_text(str(self.player.rect.x) + " - " + str(self.player.rect.y), 36, BLACK, SCREEN_WIDTH / 2, 100)
        pg.display.update()

    # Start screen
    def start_game_screen(self): 
        pg.mixer.music.load("./Resources/Sound/intro_music.ogg")
        pg.mixer.music.play(loops = -1)

        self.screen.fill(BGCOLOR)
        self.draw_text(TITLE, 48, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.draw_text("Arrows to move, Space to jump", 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.draw_text("Press a key to play", 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4)
        self.draw_text("High Score: " + str(self.highscore), 22, WHITE, SCREEN_WIDTH / 2, 15)
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
        self.draw_text("GAME OVER", 48, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.draw_text("Score: " + str(self.score), 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.draw_text("Press a key to play again", 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4)

        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("NEW HIGH SCORE!", 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 40)

            # Write new highscore to file
            with open(HIGHSCORE_FILE) as f:
                f.write(str(self.score)) 
        else:
            self.draw_text("High Score: " + str(self.highscore), 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 40)
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