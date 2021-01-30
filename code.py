import board
import random
import time

from digitalio import DigitalInOut, Direction

PRESS3 = DigitalInOut(board.BUTTON_3)
PRESS2 = DigitalInOut(board.BUTTON_2)
PRESS1 = DigitalInOut(board.BUTTON_1)
PRESS_JOYSTICK = DigitalInOut(board.SWITCH_PRESS)
userChoice = "None"
wioChoice = ""
choices = ["Rock","Paper","Scissors"]

def light():
    if PRESS_JOYSTICK.value == False:
        time.sleep(0.3)
        if board.DISPLAY.brightness == 1:
            board.DISPLAY.brightness = 0
        else:
            board.DISPLAY.brightness = 1


def returnChoice():
    global userChoice 
    if PRESS3.value == False:
        time.sleep(0.3)
        userChoice = "Rock"
        return userChoice

    if PRESS2.value == False:
        time.sleep(0.3)
        userChoice = "Paper"
        return userChoice

    if PRESS1.value == False:
        time.sleep(0.3)
        userChoice = "Rock"
        return userChoice

def returnWio():
    global wioChoice
    wioChoice = random.choice(choices)
    print("I choose... " + wioChoice + "!")
    return wioChoice

 

def printButton(userChoice):
    print("You chose...." + userChoice + "!")
    

while True:
    returnChoice()
    while userChoice != "None":
        printButton(userChoice)
        returnWio()
        break
    userChoice = "None"
    light()
