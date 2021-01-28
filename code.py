import board
import random
import time

from digitalio import DigitalInOut, Direction

PRESS3 = DigitalInOut(board.BUTTON_3)
PRESS2 = DigitalInOut(board.BUTTON_2)
PRESS1 = DigitalInOut(board.BUTTON_1)
PRESS_JOYSTICK = DigitalInOut(board.SWITCH_PRESS)
USERVALUE = ""
wioChoice = ""
choices = ["Rock","Paper","Scissors"]

def light():
    if PRESS_JOYSTICK.value == False:
        time.sleep(0.3)
        if board.DISPLAY.brightness == 1:
            board.DISPLAY.brightness = 0
        else:
            board.DISPLAY.brightness = 1

def wiochoose():
    wioChoice = random.choice(choices)
    print("I choose... " + wioChoice + "!")
#    return wioChoice

def choosePrint(choice1):
    while choice1 != "":
        print(choice1)

def choose():
    if PRESS3.value == False:
        time.sleep(0.3)
        USERVALUE = "Rock"
        print("You chose... " + USERVALUE)
        wiochoose()
        return USERVALUE

    if PRESS2.value == False:
        time.sleep(0.3)
        USERVALUE = "Paper"
        print("You chose... " + USERVALUE)
        wiochoose()
        return USERVALUE
    if PRESS1.value == False:
        time.sleep(0.3)
        USERVALUE = "Scissors"
        print("You chose... " + USERVALUE)
        wiochoose()
        return USERVALUE



def adjudicate(choice1,choice2):
    "Who wins?"

while True:
    choose()
    #choosePrint(USERVALUE)
    light()
