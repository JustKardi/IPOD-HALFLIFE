from machine import pin
import time
import struct

# BUTTONS
BUTTON_LEFT = 34
BUTTON_UP = 36
BUTTON_RIGHT = 35
BUTTON_DOWN = 39
BUTTON_CENTER = 13

BUTTON_BOOT = 0

# DISPLAY
OLED_CS = 27
OLED_RS = 21
OLED_SCL = 32
OLED_SCA = 33
OLED_RST = 19

# SD
SD_CMD = 15
SD_CLK = 14
SD_DAT0 = 2

# PCM
PCM_DIN = 22
PCM_BCK = 26
PCM_LRCK = 25
