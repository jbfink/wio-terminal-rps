import board
import random
import time

from digitalio import DigitalInOut, Direction

PRESS3 = DigitalInOut(board.BUTTON_3)
PRESS2 = DigitalInOut(board.BUTTON_2)
PRESS1 = DigitalInOut(board.BUTTON_1)
PRESS_JOYSTICK = DigitalInOut(board.SWITCH_PRESS)
button = "None"
def light():
    if PRESS_JOYSTICK.value == False:
        time.sleep(0.3)
        if board.DISPLAY.brightness == 1:
            board.DISPLAY.brightness = 0
        else:
            board.DISPLAY.brightness = 1


def returnButton():
    global button
    if PRESS3.value == False:
        time.sleep(0.3)
        button = "Rock"
        return button

    if PRESS2.value == False:
        time.sleep(0.3)
        button = "Paper"
        return button

    if PRESS1.value == False:
        time.sleep(0.3)
        button = "Rock"
        return button

def printButton(button):
    print("You chose...." + button + "!")
    

while True:
    returnButton()
    while button != "None":
        printButton(button)
        break
    button = "None"
    light()
