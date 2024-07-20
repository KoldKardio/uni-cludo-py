import os, random

# Variables: game state
gameRun = True # gamestate == run
gameMenu = True
rules = False
play = False

# entities: var
e_list = ['Red', 'Blue', 'Green', 'Yello']
playStat = {
    'Red':{'spike': 4},
    'Blue':{'spike': 4},
    'Green':{'spike': 4},
    'Yello':{'spike': 4}
}

# creation of map
boardMap = [
    # ["-1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "x9", "x10", "11", "12", "13", "14", "15", "16"],
    [" R", " R", " R", " R", " R", " R", " -", " -", " -", " B", " B", " B", " B", " B", " B"],
    [" R", "  ", "  ", "  ", "  ", " R", " -", " -", " *", " B", "  ", "  ", "  ", "  ", " B"],
    [" R", "  ", " #", " #", "  ", " R", " *", " -", " -", " B", "  ", " &", " &", "  ", " B"],
    [" R", "  ", " #", " #", "  ", " R", " -", " -", " -", " B", "  ", " &", " &", "  ", " B"],
    [" R", "  ", "  ", "  ", "  ", " R", " -", " -", " -", " B", "  ", "  ", "  ", "  ", " B"],
    [" R", " R", " R", " R", " R", " R", " -", " -", " -", " B", " B", " B", " B", " B", " B"],
    [" -", " *", " -", " -", " -", " -", " X", " .", " X", " -", " -", " -", " *", " -", " -"],
    [" -", " -", " -", " -", " -", " -", " .", " H", " .", " -", " -", " -", " -", " -", " -"],
    [" -", " -", " *", " -", " -", " -", " X", " .", " X", " -", " -", " -", " -", " *", " -"],
    [" Y", " Y", " Y", " Y", " Y", " Y", " -", " -", " -", " G", " G", " G", " G", " G", " G"],
    [" Y", "  ", "  ", "  ", "  ", " Y", " -", " -", " -", " G", "  ", "  ", "  ", "  ", " G"],
    [" Y", "  ", " @", " @", "  ", " Y", " -", " -", " -", " G", "  ", " $", " $", "  ", " G"],
    [" Y", "  ", " @", " @", "  ", " Y", " -", " -", " *", " G", "  ", " $", " $", "  ", " G"],
    [" y", "  ", "  ", "  ", "  ", " Y", " *", " -", " -", " G", "  ", "  ", "  ", "  ", " G"],
    [" Y", " Y", " Y", " Y", " Y", " Y", " -", " -", " -", " G", " G", " G", " G", " G", " G"],
    ]

# function to draw the map
def drawMap():
    for row in range( 15):
        for col in range( 15):
            print(boardMap[row][col], end = ' ')
        print(' ')
        
# coordinates
x, y = 0, 0
y_len = len(boardMap)-1
x_len = len(boardMap[0])-1

# functions: os-builtins and extra
def osClear():
    os.system('cls')
def drawLn():
    print("xx--------------------------------xx")
def g_intro():
    print("xx--------------------------------xx\n"+"---------     CLUD0.PY     ---------\n"+"xx--------------------------------xx ")
    print(" - Player 1 is 'Red'.")    
    print(" - Player 2 is 'Blue'.")    
    print(" - Player 3 is 'Green'.")    
    print(" - Player 4 is 'Yellow'.")    
    drawLn()
    print(">: 'Enter' to continue.")    
    drawLn()
    input("#: ")
def demo():
    pass
# inGame functions
def diceRoll():
    return random.randint(1, 6)
# print(diceRoll())
# inGame functions

# Game-Loop
while gameRun:
    # gameMenu
    while gameMenu:
        # menu overlay
        osClear()
        print("xx--------------------------------xx\n"+"---------     CLUD0.PY     ---------\n"+"xx--------------------------------xx ")
        drawLn()
        print('1: NEW GAME')
        print('2: RULES')
        print('3: QUIT')
        drawLn()
        
        # checking rules: demo
        if rules:
            print('Just a demo game!')
            print(diceRoll())
            rules = False
            choice = ""
            input(">: Press 'Enter' to go back...")
        else:
            choice = input("#: ")
        
        # user input: choices
        if choice == '1':
            osClear()
            g_intro() # holds some info
            gameMenu = False
            play = True
        if choice == '2':
            osClear()
            rules = True
        if choice == '3':
            quit()
        
    # playGame
    while play:
        # osClear()
        print("This is in development!")
    
    
    
    
    
    
    
    
    pass