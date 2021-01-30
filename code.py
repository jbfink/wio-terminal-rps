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
wins = 0
losses = 0
ties = 0 

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
        userChoice = "Scissors"
        return userChoice

def returnWio():
    global wioChoice
    wioChoice = random.choice(choices)
    print("I choose... " + wioChoice + "!")
    return wioChoice

 

def printButton(userChoice):
    print("You chose...." + userChoice + "!")
    
def adjudicate(choice1,choice2):
    global wins,losses,ties
    win = "YOU WIN OK!"
    lose = "YOU LOSE OK!"
    tie = "YOU TIE OK!"

    print("Go! The game is " + choice1 + " vs. " + choice2 + "!")
    if choice1 == "Rock" and choice2 == "Scissors":
        print(win)
        wins += 1

    if choice1 == "Rock" and choice2 == "Paper":
        print(lose)
        losses += 1

    if choice1 == "Rock" and choice2 == "Rock":
        print(tie)
        ties += 1

    if choice1 == "Paper" and choice2 == "Rock":
        print(win)
        wins += 1

    if choice1 == "Paper" and choice2 == "Scissors":
        print(lose)
        losses += 1

    if choice1 == "Paper" and choice2 == "Paper":
        print(tie)
        ties += 1

    if choice1 == "Scissors" and choice2 == "Paper":
        print(win)
        wins += 1

    if choice1 == "Scissors" and choice2 == "Rock":
        print(lose)
        losses +=1

    if choice1 == "Scissors" and choice2 == "Scissors":
        print(tie)
        ties += 1
    print("WINS: " + str(wins) + "  LOSSES: " + str(losses) + "  TIES: " + str(ties))

while True:
    returnChoice()
    while userChoice != "None":
        printButton(userChoice)
        returnWio()
        adjudicate(userChoice,wioChoice)
        print("----------")
        break
    userChoice = "None"
    light()
