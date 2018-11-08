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
FONT_NAME = "VNI-Lithos"
FONT_NAME_2 = "VNI-Hobo"
HIGHSCORE_FILE = "./highscores.txt"
SPRITESHEET_FILE = "./Resources/Sprites/spritesheet_jumper.png"

# Directory
SOUND_DIR = "./Resources/Sound/"
SPRITE_DIR = "./Resources/Sprites/"
BACKGROUND_DIR = "./Resources/Background/"

CAT_DIR = "./Resources/Sprites/Cat/"
CAT_DIR_2 = "./Resources/Sprites/Cat_2/"
GROUND_DIR = "./Resources/Sprites/Ground/"
TREE_DIR = "./Resources/Sprites/Tree/"
CLOUD_DIR = "./Resources/Sprites/Cloud/"
COIN_DIR = "./Resources/Sprites/Coin/"
FLAG_DIR = "./Resources/Sprites/Flag/"
BOX_DIR = "./Resources/Sprites/Box/"
ITEM_DIR = "./Resources/Sprites/Item/"

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

GROUND_LIST_TYPE2 = [(3660, MAP_HEIGHT * 0.6 - 550),
                    (4100, MAP_HEIGHT * 0.6 - 550),
                    #(4532, MAP_HEIGHT * 0.6 - 550)
                    ]
                    

GROUND_TYPE3_WIDTH = 380
 # Y: 144 with 0.8 acc
 # X: 615
 # jump max: 180
GROUND_LIST_TYPE3 = [(700, MAP_HEIGHT * 0.75),
                    #(900, MAP_HEIGHT * 0.75),
                    (900 + GROUND_TYPE3_WIDTH * 3/4, MAP_HEIGHT * 0.75),
                    (900 + GROUND_TYPE3_WIDTH * 3/4, MAP_HEIGHT * 0.45),
                    (1770, MAP_HEIGHT * 0.6),
                    (2940, MAP_HEIGHT * 0.56),
                    #(3510, MAP_HEIGHT * 0.6),
                    #(4080, MAP_HEIGHT * 0.7),
                    (5220, MAP_HEIGHT * 0.6),
                    (5600, MAP_HEIGHT * 0.18),
                    #(5790, MAP_HEIGHT * 0.6),

                    (6500, MAP_HEIGHT * 0.45)]

GROUND_LIST_TYPE4 = [(2180, MAP_HEIGHT * 0.45, 4),
                    (2560, MAP_HEIGHT * 0.3, 4),
                    (3510 - 500, MAP_HEIGHT * 0.6 - 500, 4),
                    (3510, MAP_HEIGHT * 0.6, 4),
                    (3510 + 250, MAP_HEIGHT * 0.6 - 140, 4),
                    (3510, MAP_HEIGHT * 0.6 - 140 - 160, 4),
                    (3510 - 200 , MAP_HEIGHT * 0.6 - 460, 4),
                    (3800, MAP_HEIGHT * 0.75, 4),
                    (4500, MAP_HEIGHT * 0.62, 4, True), # can move left right
                    (5200, MAP_HEIGHT * 0.18, 4),
                    (5790, MAP_HEIGHT * 0.6, 4),
                    (5590, MAP_HEIGHT * 0.75, 4),
                    (6150, MAP_HEIGHT * 0.44, 4, False, True)] # can move up down

# Number of clouds
CLOUD_NUMBER = 30

# List of trees position
TREE_LIST = [(7200, MAP_HEIGHT - 675),]

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

# List of boxs position
BOX_LIST = [(2180 + 70, MAP_HEIGHT * 0.45 - 60, 2),
            (2560 + 70, MAP_HEIGHT * 0.3 - 60, 3),
            (3510 - 500 + 70, MAP_HEIGHT * 0.6 - 500 - 60, 1),
            #(3510 + 70, MAP_HEIGHT * 0.6 - 60, 4),
            #(3510 + 250 + 70, MAP_HEIGHT * 0.6 - 140 - 60, 4),
            #(3510 + 70, MAP_HEIGHT * 0.6 - 140 - 160 - 60, 4),
            #(3510 - 200 + 70, MAP_HEIGHT * 0.6 - 460 - 60, 4),
            (3800 + 70, MAP_HEIGHT * 0.75 - 60, 3),
            (4150, 40, 4),
            (5200 + 70, MAP_HEIGHT * 0.18 - 60, 4),
            #(5790 + 70, MAP_HEIGHT * 0.6 - 60, 3),
            (5590 + 70, MAP_HEIGHT * 0.75 - 60, 3)
            ]

# List of dragonfly position
DRAGONFLY_LIST = [(1000, MAP_HEIGHT * 0.52),
                (1250, MAP_HEIGHT * 0.22),
                (2500, MAP_HEIGHT * 0.65),
                (3000, MAP_HEIGHT * 0.4),
                (4700, MAP_HEIGHT * 0.35),
                (5800, MAP_HEIGHT * 0.25),
                (7000, MAP_HEIGHT * 0.7),
                (7600, MAP_HEIGHT * 0.36)]

# List of birds position
BIRD_LIST = [(2800, 30),
            (4400, MAP_HEIGHT * 0.75),
            (4600, MAP_HEIGHT * 0.5),     
            (4700, MAP_HEIGHT * 0.18),
            (5500, MAP_HEIGHT * 0.08),
            (6400, MAP_HEIGHT * 0.36),
            (7000, MAP_HEIGHT * 0.55)]

# List of chickens position
CHICKEN_LIST = [(1500, MAP_HEIGHT * 0.86),
                (3500, MAP_HEIGHT * 0.86),
                (4140, 10),  # On sky
                (5600, MAP_HEIGHT * 0.86),
                (7550, MAP_HEIGHT * 0.86)]

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
GRAY = (64, 64, 64)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = LIGHTBLUE