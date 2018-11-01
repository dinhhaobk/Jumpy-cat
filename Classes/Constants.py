##############################################
#	Assignment 3 - Game Programming - HK181
#
#   Group 4:
#   Pham Quang Minh - 1512016
#   Nguyen Dinh Hao - 1510896
#   Vu Anh Tuan - 1513888
############################################

# Game options/settings
TITLE = "Jumpy Cat"
FULL_TITLE = "Jumpy Cat - Assignment 3 - Group 4"
WIDTH = 800
HEIGHT = 600
FPS = 60
FONT_NAME = "arial"
HIGHSCORE_FILE = "highscores.txt"
SPRITESHEET_FILE = "./Resources/Sprites/spritesheet_jumper.png"
CAT_DIR = "./Resources/Sprites/Cat/"

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 18
PLAYER_SCALE = [60, 90]

# List of grounds
GROUND_LIST_TYPE1 = [(0, HEIGHT - 60),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4 - 50),
                 (125, HEIGHT - 350),
                 (350, 200),
                 (175, 100)]
GROUND_LIST_TYPE2 = []
GROUND_LIST_TYPE3 = []
GROUND_LIST_TYPE4 = []

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = LIGHTBLUE