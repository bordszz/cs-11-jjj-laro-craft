import Scripts

WaitTime = 1

Player = {
    "xPos": 1,
    "yPos": 1,
    "mushroom": 0,
    "char": "L",
    "axe": 0,
    "flamethrower": 0,
}

InitialPlayer = { 
    "xPos": 1,
    "yPos": 1,
    "mushroom": 0,
    "char": "L",
    "axe": 0,
    "flamethrower": 0,
}


DisplayBoard = [
    ["T", "T", "T", "T", "T", "T", "T"],
    ["T", ".", ".", ".", ".", "x", "T"],
    ["T", "T", "T", "T", "T", "T", "T"],
    ["T", "T", "T", "T", "T", ".", "T"],
    ["T", "~", "~", "+", "T", "+", "T"],
    ["T", "+", "~", "R", "T", ".", "T"],
    ["T", ".", "~", "+", "T", "*", "T"],
    ["T", "T", "T", "T", "T", "T", "T"]
]

InitialBoard = [
    ["T", "T", "T", "T", "T", "T", "T"],
    ["T", ".", ".", ".", ".", "x", "T"],
    ["T", "T", "T", "T", "T", "T", "T"],
    ["T", "T", "T", "T", "T", ".", "T"],
    ["T", "~", "~", "+", "T", "+", "T"],
    ["T", "+", "~", "R", "T", ".", "T"],
    ["T", ".", "~", "+", "T", "*", "T"],
    ["T", "T", "T", "T", "T", "T", "T"]
]

ToggleBoard = [
    ["T", "T", "T", "T", "T", "T", "T"],
    ["T", ".", ".", ".", ".", "x", "T"],
    ["T", "T", "T", "T", "T", "T", "T"],
    ["T", "T", "T", "T", "T", ".", "T"],
    ["T", "~", "~", "+", "T", "+", "T"],
    ["T", "+", "~", "R", "T", ".", "T"],
    ["T", ".", "~", "+", "T", "*", "T"],
    ["T", "T", "T", "T", "T", "T", "T"]
]

while True:
    Scripts.clearConsole()
    Scripts.Position(DisplayBoard, Player)
    Scripts.printBoard(DisplayBoard)
    Scripts.PlayerInput(Player, InitialPlayer, DisplayBoard, InitialBoard, ToggleBoard, WaitTime)