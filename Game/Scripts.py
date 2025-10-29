import os
import time

def printBoard(Board):
    for count in Board:
        print(" ".join(count))

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def DenyMove(waitTime):
    print("Cannot move!!")
    time.sleep(waitTime)

def Position(Board, Player):
    Board[Player["yPos"]][Player["xPos"]] = Player["char"]

def PlayerInput(Board, Player, waitTime, Initial):
    print("\nPress W, A, S, D or I, J, K, L to move")
    print("Press ! to Restart and Q to quit")
    print('INVENTORY:')
    print("\nCurrent Mushrooms: ", Player["mushrooms"])
    print(f'Axes: {Player['axe']}')
    moveset = input("Enter move:")
    for move in moveset: 
        if move.lower() == "w" or move.lower() == "i":
            if Board[Player["yPos"] - 1][Player["xPos"]] == ".":
                Board[Player["yPos"]][Player["xPos"]] = "."
                Player["yPos"] -= 1
            elif Board[Player["yPos"]-1][Player["xPos"]] == "T": #for moving into a tree
                if Player["axe"] > 0: #checks PlayerDict if u have axe
                    Board[Player["yPos"]][Player["xPos"]] = "."
                    Player["yPos"] -= 1
                    Player["axe"] -= 1
                else:
                    DenyMove(waitTime)
            elif Board[Player["yPos"] - 1][Player["xPos"]] == "+":
                Player["mushrooms"] += 1
                Board[Player["yPos"]][Player["xPos"]] = "."
                Player["yPos"] -= 1
            elif Board[Player["yPos"] - 1][Player["xPos"]] == "~":
                Board[Player["yPos"]][Player["xPos"]] = "."
                Player["yPos"] -= 1
                Position(Board, Player)
                clearConsole()
                printBoard(Board)
                print("Game Over...")
                quit()
            else:
                DenyMove(waitTime)
            
        if move.lower() == "a" or move.lower() == "j":
            if Board[Player["yPos"]][Player["xPos"] - 1] == ".":
                Board[Player["yPos"]][Player["xPos"]] = "."
                Player["xPos"] -= 1
            elif Board[Player["yPos"]][Player["xPos"]-1] == "T": #for moving into a tree
                if Player["axe"] > 0: #checks PlayerDict if u have axe
                    Board[Player["yPos"]][Player["xPos"]] = "."
                    Player["xPos"] -= 1
                    Player["axe"] -= 1
                else:
                    DenyMove(waitTime)
            elif Board[Player["yPos"]][Player["xPos"] - 1] == "+":
                Player["mushrooms"] += 1
                Board[Player["yPos"]][Player["xPos"]] = "."
                Player["xPos"] -= 1
            elif Board[Player["yPos"]][Player["xPos"] - 1] == "~":
                Board[Player["yPos"]][Player["xPos"]] = "."
                Player["xPos"] -= 1
                Position(Board, Player)
                clearConsole()
                printBoard(Board)
                print("Game Over...")
                quit()
            else:
                DenyMove(waitTime)

        if move.lower() == "s" or move.lower() == "k":
            if Board[Player["yPos"] + 1][Player["xPos"]] == ".":
                Board[Player["yPos"]][Player["xPos"]] = "."
                Player["yPos"] += 1
            elif Board[Player["yPos"]+1][Player["xPos"]] == "T": #for moving into a tree
                if Player["axe"] > 0: #checks PlayerDict if u have axe
                    Board[Player["yPos"]][Player["xPos"]] = "."
                    Player["yPos"] += 1
                    Player["axe"] -= 1
                else:
                    DenyMove(waitTime)
            elif Board[Player["yPos"] + 1][Player["xPos"]] == "+":
                Player["mushrooms"] += 1
                Board[Player["yPos"]][Player["xPos"]] = "."
                Player["yPos"] += 1
            elif Board[Player["yPos"] + 1][Player["xPos"]] == "~":
                Board[Player["yPos"]][Player["xPos"]] = "."
                Player["yPos"] += 1
                Position(Board, Player)
                clearConsole()
                printBoard(Board)
                print("Game Over...")
                quit()
            else:
                DenyMove(waitTime)

        if move.lower() == "d" or move.lower() == "l":
            if Board[Player["yPos"]][Player["xPos"] + 1] == ".":
                Board[Player["yPos"]][Player["xPos"]] = "."
                Player["xPos"] += 1
            elif Board[Player["yPos"]][Player["xPos"]+1] == "T": #for moving into a tree
                if Player["axe"] > 0: #checks PlayerDict if u have axe
                    Board[Player["yPos"]][Player["xPos"]] = "."
                    Player["xPos"] += 1
                    Player["axe"] -= 1
                else:
                    DenyMove(waitTime)
            elif Board[Player["yPos"]][Player["xPos"] + 1] == "+":
                Player["mushrooms"] += 1
                Board[Player["yPos"]][Player["xPos"]] = "."
                Player["xPos"] += 1
            elif Board[Player["yPos"]][Player["xPos"] + 1] == "~":
                Board[Player["yPos"]][Player["xPos"]] = "."
                Player["xPos"] += 1
                Position(Board, Player)
                clearConsole()
                printBoard(Board)
                print("Game Over...")
                quit()
            else:
                DenyMove(waitTime)

        if move == "!":
            Board[Player["yPos"]][Player["xPos"]] = "."
            Player["xPos"] = Initial[1]
            Player["yPos"] = Initial[2]

        if move.lower() == "q":
            print("Goodbye")
            quit()