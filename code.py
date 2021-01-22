import board
import random
import time

from digitalio import DigitalInOut, Direction

PRESS3 = DigitalInOut(board.BUTTON_3)
PRESS2 = DigitalInOut(board.BUTTON_2)
PRESS1 = DigitalInOut(board.BUTTON_1)
PRESS_JOYSTICK = DigitalInOut(board.SWITCH_PRESS)
USERVALUE = ""

def light():
    if board.DISPLAY.brightness == 1:
        board.DISPLAY.brightness = 0
    else:
        board.DISPLAY.brightness = 1

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

while True:
    choose()
    if PRESS_JOYSTICK.value == False:
        time.sleep(0.3)
        light()

