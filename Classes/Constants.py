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
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
MAP_WIDTH = 8000
MAP_HEIGHT = 1080
FPS = 60
FONT_NAME = "arial"
HIGHSCORE_FILE = "highscores.txt"
SPRITESHEET_FILE = "./Resources/Sprites/spritesheet_jumper.png"

# Directory
CAT_DIR = "./Resources/Sprites/Cat/"
GROUND_DIR = "./Resources/Sprites/Ground/"
CLOUD_DIR = "./Resources/Sprites/Cloud/"
COIN_DIR = "./Resources/Sprites/Coin/"
FLAG_DIR = "./Resources/Sprites/Flag/"

BIRD_DIR = "./Resources/Sprites/Bird/"
DRAGONFLY_DIR = "./Resources/Sprites/Dragonfly/"
CHICKEN_DIR = "./Resources/Sprites/Chicken/"

# Player properties
PLAYER_ACC = 0.7 #0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 18
PLAYER_SCALE = [60, 90]

# List of grounds position
GROUND_LIST_TYPE1 = [(0, MAP_HEIGHT - 85),
                    (1022, MAP_HEIGHT - 85),
                    (1022 * 2 + 650, MAP_HEIGHT - 85),
                    (1022 * 3, MAP_HEIGHT - 85),
                    #(1022 * 4, MAP_HEIGHT - 85),
                    (1022 * 5, MAP_HEIGHT - 85),
                    #(1022 * 6, MAP_HEIGHT - 85),
                    (1022 * 7 - 100, MAP_HEIGHT - 85)]

GROUND_LIST_TYPE2 = [(3710, MAP_HEIGHT * 0.6 - 550),
                    (4021, MAP_HEIGHT * 0.6 - 550),
                    (4532, MAP_HEIGHT * 0.6 - 550)]
                    

GROUND_TYPE3_WIDTH = 380
 # Y: 144 with 0.8 acc
 # X: 615
 # jump max: 180
GROUND_LIST_TYPE3 = [(400, MAP_HEIGHT * 0.75),
                    (900, MAP_HEIGHT * 0.75),
                    (900 + GROUND_TYPE3_WIDTH * 3/4, MAP_HEIGHT * 0.75),
                    (1770, MAP_HEIGHT * 0.6),
                    (2940, MAP_HEIGHT * 0.56),
                    #(3510, MAP_HEIGHT * 0.6),
                    #(4080, MAP_HEIGHT * 0.7),
                    (5220, MAP_HEIGHT * 0.6),
                    #(5790, MAP_HEIGHT * 0.6),
                    (6360, MAP_HEIGHT * 0.45)]

GROUND_LIST_TYPE4 = [(2180, MAP_HEIGHT * 0.45),
                    (2560, MAP_HEIGHT * 0.3),
                    (3510, MAP_HEIGHT * 0.6),
                    (3510 + 250, MAP_HEIGHT * 0.6 - 140),
                    (3510, MAP_HEIGHT * 0.6 - 140 - 160),
                    (3510 - 200 , MAP_HEIGHT * 0.6 - 460),
                    (3800, MAP_HEIGHT * 0.75),
                    (4080, MAP_HEIGHT * 0.62), # can move left right
                    (5790, MAP_HEIGHT * 0.6),
                    (5590, MAP_HEIGHT * 0.75),
                    (6150, MAP_HEIGHT * 0.72)] # can move up down

# Number of clouds
CLOUD_NUMBER = 30

# List of coins position
COIN_LIST = [(475, MAP_HEIGHT- 225),
            (575, MAP_HEIGHT - 225),
            (675, MAP_HEIGHT- 225),
            (975, MAP_HEIGHT - 225),
            (1075, MAP_HEIGHT- 225),
            (1175, MAP_HEIGHT- 225),]

# List of flags position
FLAG_LIST = [(50, MAP_HEIGHT - 320),
            (2800, MAP_HEIGHT - 320),
            (5200, MAP_HEIGHT - 320),
            (7800, MAP_HEIGHT - 320, 1),]

# List of dragonfly position
DRAGONFLY_LIST = [(400, MAP_HEIGHT - 400),]

# List of birds position
BIRD_LIST = [(700, MAP_HEIGHT- 400),]

# List of chickens position
CHICKEN_LIST = [(2000, MAP_HEIGHT - 150)]

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = LIGHTBLUE