import board
import random
import time

from digitalio import DigitalInOut, Direction

PRESS3 = DigitalInOut(board.BUTTON_3)
PRESS2 = DigitalInOut(board.BUTTON_2)
PRESS1 = DigitalInOut(board.BUTTON_1)
PRESS_JOYSTICK = DigitalInOut(board.SWITCH_PRESS)
USERVALUE = ""
choices = ["r","p","s"]

def light():
    if PRESS_JOYSTICK.value == False:
        time.sleep(0.3)
        if board.DISPLAY.brightness == 1:
            board.DISPLAY.brightness = 0
        else:
            board.DISPLAY.brightness = 1

def wiochoose():
    print(random.choice(choices))

def choose():
    if PRESS3.value == False:
        time.sleep(0.3)
        USERVALUE = "Rock"
        print(USERVALUE)
    if PRESS2.value == False:
        time.sleep(0.3)
        USERVALUE = "Paper"
        print(USERVALUE)
    if PRESS1.value == False:
        time.sleep(0.3)
        USERVALUE = "Scissors"
        print(USERVALUE)

#    wiochoose()
#    the above line currently just spews out choices without waiting. will fix.

while True:
    choose()
    light()
