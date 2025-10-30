#WHAT I CHANGED:
# changed movement
# changed restart to refer to RestartBoard instead of InitialBoard
# inital board can be mutated now for the items and mushrooms

import os
import time
import copy

def printBoard(Board):
    for count in Board:
        print(" ".join(count))

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear') #so that it works for macOS too

def DenyMove(waitTime):
    print("Cannot move!!")
    time.sleep(waitTime)

def DenyPickup(waitTime):
    print("No item under you!!")
    time.sleep(waitTime)

def UsedAxe(waitTime):
    print("1 Axe was used")
    time.sleep(waitTime)

def Position(Board, Player):
    Board[Player["yPos"]][Player["xPos"]] = Player["char"]

def Restart(RestartBoard, Board, InitialPlayer, Player):
    Board[:] = copy.deepcopy(RestartBoard)
    Player.clear()
    Player.update(copy.deepcopy(InitialPlayer))

def ConsumeMushroom(InitialBoard, Player):
    if InitialBoard[Player["yPos"]][Player["xPos"]] == '+':
        InitialBoard[Player["yPos"]][Player["xPos"]] = '.'
        Player['mushrooms'] += 1
    else:
        pass

def PickedUp(InitalBoard, Player):
    if InitialBoard[Player["yPos"]][Player["xPos"]] in ('A', 'F'):
        InitialBoard[Player["yPos"]][Player["xPos"]] = '.'
    else:
        pass

def PlayerInput(Board, Player, waitTime, InitialPlayer, InitialBoard):
    print("\nPress W, A, S, D or I, J, K, L to move")
    print("Press E to pickup an item, ! to Restart and Q to quit")
    print("\nCurrent Mushrooms: ", Player["mushrooms"])
    print(f'Axes: {Player['axe']}')
    print(f'Flamethrowers: {Player['flamethrower']}')
    moveset = input("Enter move:")
    for move in moveset: 
        #UP and DOWN 
        y_mvmnt = {'w':-1, 'i':-1, 's':1, 'k':1}
        x_mvmnt = {'a':-1, 'j':-1, 'd':1, 'l':1}
        if move.lower() in ('w', 'i', 's', 'k'):
            ConsumeMushroom(InitialBoard, Player)
            if Board[Player["yPos"] + y_mvmnt[move.lower()]][Player["xPos"]] == 'T': #if ur moving into a tree
                if Player['axe'] >= 1:
                    Board[Player["yPos"] + y_mvmnt[move.lower()]][Player["xPos"]] = '.'
                    InitialBoard[Player["yPos"] + y_mvmnt[move.lower()]][Player["xPos"]] = '.'
                    Player['axe'] -= 1
                    UsedAxe(waitTime)
                else:
                    DenyMove(waitTime)

            else: #if ur not moving into a tree (normal)
                Board[Player["yPos"]][Player["xPos"]] = InitialBoard[Player["yPos"]][Player["xPos"]]
                Player['yPos'] += y_mvmnt[move.lower()]

        #LEFT and RIGHT
        elif move.lower() in ('a', 'j', 'd', 'l'):
            ConsumeMushroom(InitialBoard, Player)
            if Board[Player["yPos"]][Player["xPos"]+ x_mvmnt[move.lower()]] == 'T': #if ur moving into a tree
                if Player['axe'] >= 1:
                    Board[Player["yPos"]][Player["xPos"] + x_mvmnt[move.lower()]] = '.'
                    InitialBoard[Player["yPos"]][Player["xPos"]+ x_mvmnt[move.lower()]] = '.'
                    Player['axe'] -= 1
                    UsedAxe(waitTime)
                else:
                    DenyMove(waitTime)

            else: #if ur not moving into a tree (normal)
                Board[Player["yPos"]][Player["xPos"]] = InitialBoard[Player["yPos"]][Player["xPos"]] 
                Player['xPos'] += x_mvmnt[move.lower()]


        #PICKUP FUNCTION
        if move.lower() == 'e': 
            if InitialBoard[Player["yPos"]][Player["xPos"]] == 'A':
                PickedUp(InitialBoard, Player)
                Player['axe'] += 1
            elif InitialBoard[Player["yPos"]][Player["xPos"]] == 'F':
                PickedUp(InitialBoard, Player)
                Player['flamethrower'] += 1
            else:
                DenyPickup(waitTime)
                

        #RESTART
        if move.lower() == "!":
            Restart(RestartBoard, Board, InitialPlayer, Player)
            clearConsole()
            Position(Board, Player)
            printBoard(Board)
            continue

        #QUITTING
        if move.lower() == "q":
            print("Goodbye")
            quit()

#GAME LOOP --------------------------------------------------------------------------------

waitTime = 1


Player = {
    "xPos": 3,
    "yPos": 5,
    "mushrooms": 0,
    "char": "L",
    "axe": 0,
    "flamethrower": 0,
}

Board = [
    ["T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T"],
    ["T", ".", ".", ".", "A", ".", ".", "T", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", ".", ".", "T", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", ".", ".", "T", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", "+", "+", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", "+", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", "+", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", "F", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", "+", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T"]
]


#INITIAL SETTINGS FOR RESTART FUNCTION -----------------------------------------------------------
InitialPlayer = {
    "xPos": 3,
    "yPos": 5,
    "mushrooms": 0,
    "char": "L",
    "axe": 0,
    "flamethrower": 0,
}

InitialBoard = [
    ["T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T"],
    ["T", ".", ".", ".", "A", ".", ".", "T", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", ".", ".", "T", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", ".", ".", "T", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", "+", "+", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", "+", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", "+", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", "F", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", "+", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T"]
]

RestartBoard = [
    ["T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T"],
    ["T", ".", ".", ".", "A", ".", ".", "T", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", ".", ".", "T", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", ".", ".", "T", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", "+", "+", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", "+", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", "+", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", "F", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", "+", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", "T"]
]


#---------------------------------------------------------------------------------------------------
while True:
    clearConsole()
    Position(Board, Player)
    printBoard(Board)
    PlayerInput(Board, Player, waitTime, InitialPlayer, InitialBoard)