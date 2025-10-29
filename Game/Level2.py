import Scripts

waitTime = 1

Player = {
    "xPos": 2,
    "yPos": 2,
    "mushrooms": 0,
    "char": "L",
    "axe": 0,
    "flamethrower": 0,
}


Board = [
    ["T", "T", "T", "T", "T", "T", "T", "T", "T", "T"],
    ["T", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", "+", "+", "~", "~", "~", "+", "T"],
    ["T", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", "T", "T", "T", "T", "T", "T", "T", "T", "T"]
]

InitialPlayer = { 
    "xPos": 2,
    "yPos": 2,
    "mushrooms": 0,
    "char": "L",
}

InitialBoard = [
    ["T", "T", "T", "T", "T", "T", "T", "T", "T", "T"],
    ["T", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", ".", ".", "+", "+", "~", "~", "~", "+", "T"],
    ["T", ".", ".", ".", ".", ".", ".", ".", ".", "T"],
    ["T", "T", "T", "T", "T", "T", "T", "T", "T", "T"]
]

while True:
    Scripts.clearConsole()
    Scripts.Position(Board, Player)
    Scripts.printBoard(Board)
    Scripts.PlayerInput(Board, Player, waitTime, InitialPlayer, InitialBoard)