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

def Position(Board, Player):
    Board[Player["yPos"]][Player["xPos"]] = Player["char"]

def Restart(InitialBoard, Board, InitialPlayer, Player):
    Board[:] = copy.deepcopy(InitialBoard)
    Player.clear()
    Player.update(copy.deepcopy(InitialPlayer))

def PlayerInput(Board, Player, waitTime, InitialPlayer, InitialBoard):
    print("\nPress W, A, S, D or I, J, K, L to move")
    print("Press E to pickup an item, ! to Restart and Q to quit")
    print("\nCurrent Mushrooms: ", Player["mushrooms"])
    print(f'Axes: {Player['axe']}')
    print(f'Flamethrowers: {Player['flamethrower']}')
    moveset = input("Enter move:")
    for move in moveset: 
        #MOVESETS FOR UP (W/I)
        if move.lower() == "w" or move.lower() == "i":
            if Board[Player["yPos"] - 1][Player["xPos"]] == "." : #moving into open space
                if InitialBoard[Player["yPos"]][Player["xPos"]] == "+": #if previous position is on a mushroom
                    Board[Player["yPos"]][Player["xPos"]] = "."
                    Player["yPos"] -= 1
                else:
                    Board[Player["yPos"]][Player["xPos"]] = InitialBoard[Player["yPos"]][Player["xPos"]] 
                    Player["yPos"] -= 1
            elif Board[Player["yPos"] - 1][Player["xPos"]] == "+": #moving into a mushroom (autoeat)
                Player["mushrooms"] += 1
                Board[Player["yPos"]][Player["xPos"]] = InitialBoard[Player["yPos"]][Player["xPos"]]
                Player["yPos"] -= 1
            elif Board[Player["yPos"] - 1][Player["xPos"]] == "~": #moving into water (dead)
                Board[Player["yPos"]][Player["xPos"]] = InitialBoard[Player["yPos"]][Player["xPos"]]
                Player["yPos"] -= 1
                Position(Board, Player)
                clearConsole()
                printBoard(Board)
                print("Game Over...")
                quit()
            elif Board[Player["yPos"] - 1][Player["xPos"]] == "T" : #moving into a tree
                if Player['axe'] == 1:
                    Player['axe'] -= 1
                    Board[Player["yPos"]][Player["xPos"]] = InitialBoard[Player["yPos"]][Player["xPos"]] 
                    Player["yPos"] -= 1
            elif Board[Player["yPos"] - 1][Player["xPos"]] == "A" or Board[Player["yPos"]-1][Player["xPos"]] == "F": #moving into an A or F
                if InitialBoard[Player["yPos"]][Player["xPos"]] == "+": #if previous position is on a mushroom
                    Board[Player["yPos"]][Player["xPos"]] = "."
                    Player["yPos"] -= 1
                else:
                    Board[Player["yPos"]][Player["xPos"]] = InitialBoard[Player["yPos"]][Player["xPos"]] 
                    Player["yPos"] -= 1

            else:
                DenyMove(waitTime)

        #MOVESETS FOR LEFT (A/J)    
        if move.lower() == "a" or move.lower() == "j":
            if Board[Player["yPos"]][Player["xPos"] - 1] == "." : #moving into open space
                if InitialBoard[Player["yPos"]][Player["xPos"]] == "+": #if previous position is on a mushroom
                    Board[Player["yPos"]][Player["xPos"]] = "."
                    Player["xPos"] -= 1
                else:
                    Board[Player["yPos"]][Player["xPos"]] = InitialBoard[Player["yPos"]][Player["xPos"]]
                    Player["xPos"] -= 1
            elif Board[Player["yPos"]][Player["xPos"] - 1] == "+": #moving into a mushroom (autoeat)
                Player["mushrooms"] += 1
                Board[Player["yPos"]][Player["xPos"]] = "."
                Player["xPos"] -= 1
            elif Board[Player["yPos"]][Player["xPos"] - 1] == "~": #moving into water (dead)
                Board[Player["yPos"]][Player["xPos"]] = "."
                Player["xPos"] -= 1
                Position(Board, Player)
                clearConsole()
                printBoard(Board)
                print("Game Over...")
                quit()
            elif Board[Player["yPos"]][Player["xPos"] - 1] == "T" : #moving into a tree
                if Player['axe'] == 1:
                    Player['axe'] -= 1
                    Board[Player["yPos"]][Player["xPos"]] = InitialBoard[Player["yPos"]][Player["xPos"]] 
                    Player["xPos"] -= 1
            elif Board[Player["yPos"]][Player["xPos"] - 1] == "A" or Board[Player["yPos"]][Player["xPos"] - 1] == "F": #moving into an A or F
                if InitialBoard[Player["yPos"]][Player["xPos"]] == "+": #if previous position is on a mushroom
                    Board[Player["yPos"]][Player["xPos"]] = "."
                    Player["xPos"] -= 1
                else:
                    Board[Player["yPos"]][Player["xPos"]] = InitialBoard[Player["yPos"]][Player["xPos"]] 
                    Player["xPos"] -= 1

            else:
                DenyMove(waitTime)

        #MOVESETS FOR DOWN (S/K)
        if move.lower() == "s" or move.lower() == "k":
            if Board[Player["yPos"] + 1][Player["xPos"]] == "." : #moving into open space
                if InitialBoard[Player["yPos"]][Player["xPos"]] == "+": #if previous position is on a mushroom
                    Board[Player["yPos"]][Player["xPos"]] = "."
                    Player["yPos"] += 1
                else:
                    Board[Player["yPos"]][Player["xPos"]] = InitialBoard[Player["yPos"]][Player["xPos"]]
                    Player["yPos"] += 1
            elif Board[Player["yPos"] + 1][Player["xPos"]] == "+": #moving into a mushroom (autoeat)
                Player["mushrooms"] += 1
                Board[Player["yPos"]][Player["xPos"]] = "."
                Player["yPos"] += 1
            elif Board[Player["yPos"] + 1][Player["xPos"]] == "~": #moving into water (dead)
                Board[Player["yPos"]][Player["xPos"]] = "."
                Player["yPos"] += 1
                Position(Board, Player)
                clearConsole()
                printBoard(Board)
                print("Game Over...")
                quit()
            elif Board[Player["yPos"] + 1][Player["xPos"]] == "T" : #moving into a tree
                if Player['axe'] == 1:
                    Player['axe'] -= 1
                    Board[Player["yPos"]][Player["xPos"]] = InitialBoard[Player["yPos"]][Player["xPos"]] 
                    Player["yPos"] += 1
            elif Board[Player["yPos"] + 1][Player["xPos"]] == "A" or Board[Player["yPos"] + 1][Player["xPos"]] == "F": #moving into an A or F
                if InitialBoard[Player["yPos"]][Player["xPos"]] == "+": #if previous position is on a mushroom
                    Board[Player["yPos"]][Player["xPos"]] = "."
                    Player["yPos"] += 1
                else:
                    Board[Player["yPos"]][Player["xPos"]] = InitialBoard[Player["yPos"]][Player["xPos"]] 
                    Player["yPos"] += 1
            else:
                DenyMove(waitTime)
        
        #MOVESETS FOR RIGHT (D/L)
        if move.lower() == "d" or move.lower() == "l":
            if Board[Player["yPos"]][Player["xPos"] + 1] == "." : #moving into open space
                if InitialBoard[Player["yPos"]][Player["xPos"]] == "+": #if previous position is on a mushroom
                    Board[Player["yPos"]][Player["xPos"]] = "."
                    Player["xPos"] += 1
                else:
                    Board[Player["yPos"]][Player["xPos"]] = InitialBoard[Player["yPos"]][Player["xPos"]]
                    Player["xPos"] += 1
            elif Board[Player["yPos"]][Player["xPos"] + 1] == "+": #moving into a mushroom (autoeat)
                Player["mushrooms"] += 1
                Board[Player["yPos"]][Player["xPos"]] = "."
                Player["xPos"] += 1
            elif Board[Player["yPos"]][Player["xPos"] + 1] == "~": #moving into water (dead)
                Board[Player["yPos"]][Player["xPos"]] = "."
                Player["xPos"] += 1
                Position(Board, Player)
                clearConsole()
                printBoard(Board)
                print("Game Over...")
                quit()

            elif Board[Player["yPos"]][Player["xPos"]+1] == "T" : #moving into a tree
                if Player['axe'] == 1:
                    Player['axe'] -= 1
                    Board[Player["yPos"]][Player["xPos"]] = InitialBoard[Player["yPos"]][Player["xPos"]] 
                    Player["xPos"] += 1
            elif Board[Player["yPos"]][Player["xPos"]+1] == "A" or Board[Player["yPos"]][Player["xPos"]+1] == "F": #moving into an A or F
                if InitialBoard[Player["yPos"]][Player["xPos"]] == "+": #if previous position is on a mushroom
                    Board[Player["yPos"]][Player["xPos"]] = "."
                    Player["xPos"] += 1
                else:
                    Board[Player["yPos"]][Player["xPos"]] = InitialBoard[Player["yPos"]][Player["xPos"]] 
                    Player["xPos"] += 1
            else:
                DenyMove(waitTime)

        #PICKUP FUNCTION
        elif move.lower() == 'e': 
            if Player['axe'] + Player['flamethrower'] == 0:
                if InitialBoard[Player["yPos"]][Player["xPos"]] == 'A': #PICKING UP AN AXE
                    Player['axe'] += 1
                    #i want to update the InitialBoard, but it wil mess up the restart function. but if u dont mind that, uncomment this code
                    InitialBoard[Player["yPos"]][Player["xPos"]] = '.'
                elif InitialBoard[Player["yPos"]][Player["xPos"]] == 'F': #PICKING UP A FLAMETHROWER
                    Player['flamethrower'] += 1
                    #i want to update the InitialBoard, but it wil mess up the restart function. but if u dont mind that, uncomment this code
                    InitialBoard[Player["yPos"]][Player["xPos"]] = '.'
                else:
                    pass
            else:
                pass


        #RESTART
        if move.lower() == "!":
            Restart(InitialBoard, Board, InitialPlayer, Player)
            clearConsole()
            Position(Board, Player)
            printBoard(Board)
            continue

        #QUITTING
        if move.lower() == "q":
            print("Goodbye")
            quit()