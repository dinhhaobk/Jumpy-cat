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
from Classes.Sound import Sound
from Classes.Object.Player import Player
from Classes.Object.Ground import Ground
from Classes.Object.Tree import Tree
from Classes.Object.Cloud import Cloud
from Classes.Object.Coin import Coin
from Classes.Object.Box import Box
from Classes.Object.Flag import Flag
from Classes.Object.Dragonfly import Dragonfly
from Classes.Object.Bird import Bird
from Classes.Object.Chicken import Chicken

class Game:
    def __init__(self):
        # Init game window, title, clock, font, data
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        pg.display.set_caption(FULL_TITLE)
        pg.mouse.set_visible(False)
        self.clock = pg.time.Clock()
        self.font_name = pg.font.match_font(FONT_NAME)  
        self.font_name_2 = pg.font.match_font(FONT_NAME_2)   

        # Variable used for loop - while
        self.isWaitingStartScreen = True
        self.isWaitingEndScreen = True
        self.isPlayingGame = True
        self.isRunningWindow = True
        
        self.chooseStart = 1 # Used for triangle image on start screen
        self.chooseOption = 3 # Used for triangle image on option screen

        # Used for choosing in option screen
        self.optionCharacter = 1
        self.optionMusic = True
        self.optionSound = True

        # Used for which screen to draw text + image
        self.onStart = True
        self.onOption = False
        self.onCredit = False

        self.load_data()

    # Load all data
    def load_data(self):
        # Read highscore file
        with open(HIGHSCORE_FILE, 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0

        self.sound = Sound() # Load sound + music
        
    # Start a new game
    def start(self):   
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.grounds = pg.sprite.Group() # Group of ground sprites
        self.trees = pg.sprite.Group() # Group of tree sprites
        self.clouds = pg.sprite.Group() # Group of cloud sprites
        self.coins = pg.sprite.Group() # Group of coin sprites
        self.boxs = pg.sprite.Group() # Group of box sprites    
        self.flags = pg.sprite.Group() # Group of flag sprites    
        self.dragonflys = pg.sprite.Group() # Group of dragonfly sprites 
        self.birds = pg.sprite.Group() # Group of bird sprites
        self.chickens = pg.sprite.Group() # Group of chicken sprites
        
        # Init cloud
        for cloud in range(CLOUD_NUMBER):
            Cloud(self, cloud)  
        
        # Init tree
        for tree in TREE_LIST:
            Tree(self, *tree)

        # Init flag
        for flag in FLAG_LIST:
            Flag(self, *flag)

        # Init ground
        for ground2 in GROUND_LIST_TYPE1:
            Ground(self, *ground2, 1)
        for ground in GROUND_LIST_TYPE2:
            Ground(self, *ground, 2)     
        for ground3 in GROUND_LIST_TYPE3:
            Ground(self, *ground3, 3)
        for ground4 in GROUND_LIST_TYPE4:
            Ground(self, *ground4) 
     
        # Init box
        for box in BOX_LIST:
            Box(self, *box)

        # Init dragonfly
        for dragonfly in DRAGONFLY_LIST:
            Dragonfly(self, *dragonfly)

        # Init bird
        for bird in BIRD_LIST:
            Bird(self, *bird)

        # Init chicken
        for chicken in CHICKEN_LIST:
            Chicken(self, *chicken)

        # Init player
        self.player = Player(self) 
        self.camera = Camera(self.screen, self.player, MAP_WIDTH, MAP_HEIGHT) # Init camera

        self.score = 0 # Score of player
        self.isPause = False  # Check game is pause or not
        self.run()

    # Run a loop game
    def run(self):   
        self.sound.playBgMusic()

        while self.isPlayingGame:
            if self.isPause:
                pg.time.wait(100) # Pause game
                self.events()
            else:
                self.clock.tick(FPS)
                self.events()
                self.update()
                self.draw()
        self.sound.musicFadeOut()

    # Game loop - events
    def events(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if self.isPlayingGame:
                        self.isPlayingGame = False
                    self.isRunningWindow = False

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

        # Check if player falls out of map - return to flag (checkpoint)
        if self.player.pos.y > MAP_HEIGHT + 200:
            self.player.pos = self.player.checkPoint
            self.player.life -= 1

        # Check if player hits a ground (only if falling)
        if self.player.vel.y > 0:
            ground_hit_list = pg.sprite.spritecollide(self.player, self.grounds, False)
            if len(ground_hit_list) == 1:
                lowest = ground_hit_list[0]
                if (self.player.pos.x < lowest.rect.right + 10) and (self.player.pos.x > lowest.rect.left - 10):
                    if (self.player.pos.y > lowest.rect.top) and (self.player.pos.y < lowest.rect.bottom - 47 * 0.2):
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
        
        # Check if player hits a coin - kill coin, + score
        coin_list = pg.sprite.spritecollide(self.player, self.coins, False, pg.sprite.collide_mask)
        for i in range(len(coin_list)):
            coin_list[i - 1].kill()
            self.score += 50

        # Check if player hits a flag - save the checkpoint
        isHitFlag = pg.sprite.spritecollide(self.player, self.flags, False)
        if isHitFlag:
            if isHitFlag[0].type == 0:
                self.player.checkPoint = (isHitFlag[0].rect.x, isHitFlag[0].rect.y + 200)
            else:
                self.isPlayingGame = False
        
        # Check if player hits a dragonfly - kill dragonfly, + score
        dragonfly_list = pg.sprite.spritecollide(self.player, self.dragonflys, False, pg.sprite.collide_mask)
        for i in range(len(dragonfly_list)):
            dragonfly_list[i - 1].kill()
            self.score += 100

        # Check if player hits a chicken from ahead - kill chicken, + score
        chicken_list = pg.sprite.spritecollide(self.player, self.chickens, False, pg.sprite.collide_mask)
        for chick in chicken_list:
            if (self.player.rect.bottom >= chick.rect.top) and (self.player.rect.top < chick.rect.top):
                if self.player.isJump:
                    chick.kill()
                    self.score += 200
                else:
                    self.player.pos = self.player.checkPoint # Return to checkpoint - if being hit
                    self.player.life -= 1
            else:
                self.player.pos = self.player.checkPoint # Return to checkpoint - if being hit
                self.player.life -= 1

        # Check if player hits a bird - return to checkpoint
        isHitBird = pg.sprite.spritecollide(self.player, self.birds, False, pg.sprite.collide_mask)
        if isHitBird:
            self.player.pos = self.player.checkPoint
            self.player.life -= 1

        # Check if chicken hits a ground
        for chick in self.chickens:
            chicken_hit_ground_list = pg.sprite.spritecollide(chick, self.grounds, False)
            if chicken_hit_ground_list:
                chick.movy = 0
        
        # If player has 0 life - game over
        if self.player.life == 0:
            self.isPlayingGame = False

    # Game loop - draw
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.camera.draw_sprites(self.screen, self.all_sprites)
        self.draw_text(self.font_name, str(self.score), 36, WHITE, SCREEN_WIDTH / 2, 36)
        self.draw_text(self.font_name, str(self.player.rect.x) + " - " + str(self.player.rect.y), 36, BLACK, SCREEN_WIDTH / 2, 100)
        pg.display.update()

########################################################################################################
    # Start screen
    def start_game_screen(self): 
        self.sound.playIntroMusic()

        while self.isWaitingStartScreen:
            self.screen.fill(BGCOLOR)

            # If on start screen
            if self.onStart:
                self.draw_text(self.font_name, TITLE, 80, YELLOW, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 9)
                self.draw_text(self.font_name_2, "High Score: " + str(self.highscore), 40, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3.2)
                self.draw_text(self.font_name_2, "Play", 40, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.2)
                self.draw_text(self.font_name_2, "Option", 40, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.2 + 75)
                self.draw_text(self.font_name_2, "Credits", 40, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.2 + 75 * 2)
                self.draw_text(self.font_name_2, "Exit", 40, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.2 + 75 * 3)
                
                self.draw_image(SPRITE_DIR + "triangle.png", 50, 50, SCREEN_WIDTH / 2.6, SCREEN_HEIGHT / 2 + (self.chooseStart - 1) * 75 - 25)

            # If on option screen
            if self.onOption:
                self.draw_text(self.font_name, "OPTION", 80, YELLOW, SCREEN_WIDTH / 2 + 30, SCREEN_HEIGHT / 9)
                self.draw_text(self.font_name_2, "CHARACTER", 40, WHITE, SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2.5)
                self.draw_text(self.font_name_2, "MUSIC", 40, WHITE, SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2.5 + 75) 
                if self.optionMusic:
                    self.draw_text(self.font_name_2, "ON", 40, WHITE, SCREEN_WIDTH / 2 + 200, SCREEN_HEIGHT / 2.5 + 75)  
                else:
                    self.draw_text(self.font_name_2, "OFF", 40, WHITE, SCREEN_WIDTH / 2 + 200, SCREEN_HEIGHT / 2.5 + 75) 
                self.draw_text(self.font_name_2, "SOUND", 40, WHITE, SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2.5 + 75 * 2)
                if self.optionSound: 
                    self.draw_text(self.font_name_2, "ON", 40, WHITE, SCREEN_WIDTH / 2 + 200, SCREEN_HEIGHT / 2.5 + 75 * 2)  
                else:
                    self.draw_text(self.font_name_2, "OFF", 40, WHITE, SCREEN_WIDTH / 2 + 200, SCREEN_HEIGHT / 2.5 + 75 * 2)  
                self.draw_text(self.font_name_2, "Back", 40, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.2 + 250)

                if self.chooseOption == 4:
                    self.draw_image(SPRITE_DIR + "triangle.png", 50, 50, SCREEN_WIDTH / 2.6, SCREEN_HEIGHT / 1.22) 
                else:
                    self.draw_image(SPRITE_DIR + "triangle.png", 50, 50, SCREEN_WIDTH / 3.4, SCREEN_HEIGHT / 3.2 + self.chooseOption * 75)
                if self.optionCharacter == 1:
                    self.draw_image(CAT_DIR + "Idle (1).png", 60, 90, SCREEN_WIDTH / 1.58, SCREEN_HEIGHT / 2.5 - 20)
                else:
                    self.draw_image(CAT_DIR_2 + "Idle (1).png", 60, 90, SCREEN_WIDTH / 1.58, SCREEN_HEIGHT / 2.5 - 20)

            # If on credit screen
            if self.onCredit:
                self.draw_text(self.font_name, "CREDITS", 80, YELLOW, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 9)
                self.draw_text(self.font_name_2, "Nguyen Dinh Hao", 40, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.5)
                self.draw_text(self.font_name_2, "Vu Anh Tuan", 40, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.5 + 75 )
                self.draw_text(self.font_name_2, "Pham Quang Minh", 40, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.5 + 75 * 2)
                self.draw_text(self.font_name_2, "Back", 40, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.2 + 250)
                
                self.draw_image(SPRITE_DIR + "triangle.png", 50, 50, SCREEN_WIDTH / 2.6, SCREEN_HEIGHT / 2.2 + 260)

            pg.display.flip()
            self.wait_for_key_on_begin_screen()
        self.sound.musicFadeOut()

    # Waiting key events on start screen
    def wait_for_key_on_begin_screen(self):
        self.clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.isWaitingStartScreen = self.isRunningWindow = False

                elif event.key == pg.K_UP:
                    if self.onStart:
                        if self.chooseStart > 1: 
                            self.chooseStart -= 1 
                    elif self.onOption:
                        if self.chooseOption > 1: 
                            self.chooseOption -= 1 

                elif event.key == pg.K_DOWN:
                    if self.onStart:
                        if self.chooseStart < 4: 
                            self.chooseStart += 1  
                    elif self.onOption:
                        if self.chooseOption < 4:
                            self.chooseOption += 1  

                elif (event.key == pg.K_LEFT) or (event.key == pg.K_RIGHT):
                    if self.onOption:
                        if self.chooseOption == 1:
                            if self.optionCharacter == 1:
                                self.optionCharacter = 2 
                            else:                   
                                self.optionCharacter = 1

                        elif self.chooseOption == 2:
                            if self.optionMusic:
                                self.optionMusic = False 
                            else:                   
                                self.optionMusic = True

                        elif self.chooseOption == 3:
                            if self.optionSound:
                                self.optionSound = False 
                            else:                   
                                self.optionSound = True
                                
                elif event.key == pg.K_SPACE:
                    if self.onStart:
                        if self.chooseStart == 1:
                            self.isWaitingStartScreen = False
                        elif self.chooseStart == 2:
                            self.onOption = True
                            self.onStart = self.onCredit = False
                        elif self.chooseStart == 3:
                            self.onCredit = True
                            self.onStart = self.onOption = False
                        elif self.chooseStart == 4: 
                            self.isWaitingStartScreen = self.isRunningWindow = False

                    elif self.onOption:
                        if self.chooseOption == 4:
                            self.onStart = True
                            self.onOption = self.onCredit = False

                    elif self.onCredit:
                        self.onStart = True
                        self.onOption = self.onCredit = False

########################################################################################################
    # Game over screen
    def game_over_screen(self):   
        if not self.isRunningWindow:
            return
        self.sound.playIntroMusic()

        self.screen.fill(BGCOLOR)
        self.draw_text(self.font_name, "GAME OVER", 48, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.draw_text(self.font_name, "Score: " + str(self.score), 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text(self.font_name, "NEW HIGH SCORE!", 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 40)

            # Write new highscore to file
            with open(HIGHSCORE_FILE, 'w') as f:
                f.write(str(self.score)) 
        else:
            self.draw_text(self.font_name, "High Score: " + str(self.highscore), 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 40)
        
        pg.display.flip()
        #self.wait_for_key_on_begin_screen()
        self.sound.musicFadeOut()

########################################################################################################
    # Draw text
    def draw_text(self, font, text, size, color, pos_x, pos_y):
        font_to_draw = pg.font.Font(font, size)
        text_surface = font_to_draw.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (pos_x, pos_y)
        self.screen.blit(text_surface, text_rect)

    # Draw image
    def draw_image(self, file, size_x, size_y, pos_x, pos_y):
        image = pg.image.load(file)
        image_scale = pg.transform.scale(image, (size_x, size_y))
        self.screen.blit(image_scale, (pos_x, pos_y))


########################################################################################################
# Init the game
pg.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
pg.init()

myGame = Game()
while myGame.isRunningWindow:
    myGame.start_game_screen()
    if myGame.isRunningWindow:
        myGame.start()
    if myGame.isRunningWindow:
        myGame.game_over_screen()

pg.quit()