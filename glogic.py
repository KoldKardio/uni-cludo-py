# finding the game logic here
# players play each turn roll dice then move their character
import random, os

# elist = ['a', 'b', 'c']

# for item in range(3):
#     if item != 2:
#         ehold = elist[item]
#         elist[item] = elist[item+1]
#         print(item)
#     else:
#         elist[item] = 'a'

# print(elist)

# demo map : pretend 'a' is playChar
demoMap = [
    ['a', 'b', 'c'],
    ['1', '2', '3'],
    ['!', '@', '#']
]

def mapDraw():
    for row in range( 3): # x 
            # print(row)
            for col in range( 3): # y
                # print(row)
                print(demoMap[row][col], end = '  ')
            print(' ')

# moveset
moveTile = {
     'a': {
          't': 'A',
          'dir': 'right',
          'jump': False,
          'jmpDir': 'down',
     },
     'b': {
          't': 'B',
          'dir': 'right',
          'jump': False,
          'jmpDir': 'down',
     },
     'c': {
          't': 'C',
          'dir': 'right',
          'jump': True,
          'jmpDir': 'down',
     },
     '3': {
          't': '3',
          'dir': 'left',
          'jump': False,
          'jmpDir': 'down',
     },
     '2': {
          't': '2',
          'dir': 'left',
          'jump': False,
          'jmpDir': 'down',
     },
     '1': {
          't': '1',
          'dir': 'left',
          'jump': True,
          'jmpDir': 'down',
     },
     '!': {
          't': '!',
          'dir': 'right',
          'jump': False,
          'jmpDir': 'down',
     },
     '@': {
          't': '@',
          'dir': 'right',
          'jump': False,
          'jmpDir': 'down',
     },
     '#': {
          't': '#',
          'dir': 'right',
          'jump': True,
          'jmpDir': 'up',
     },
}

# coordinates
x, y= 0, 0
y_len = len(demoMap)-1
x_len = len(demoMap[0])-1
currentLoc = demoMap[y][x]

tile_name = moveTile[currentLoc]['t']

canMove = False

# dice check
def diceRoll():
    return random.randint(1, 1)
# print(diceRoll())

# to do
# move a char from one loc to another: use 5x5 loop from js or try the lanehopper meth

# gameLoop
while True:
    os.system('cls')
    mapDraw()
    # check
    print(currentLoc)
    
    # direction check
    if y > 0: print("1 - NORTH")
    if x < x_len: print("2 - EAST")
    if y < y_len: print("3 - SOUTH")
    if x > 0: print("4 - WEST")
    
    # check get input
    print("Press 1 to roll dice")
    choice = input(">: ")

    if choice == "1":
        # roll dice
        valueHold = diceRoll()
        print('--------------')
        print(valueHold)
        print('--------------')
        currentLoc = demoMap[y][x]

        if valueHold == 1 or valueHold == 2 or valueHold == 3 or canMove == True:
             print('Your player can move.')
             canMove = True      
          #    y = valueHold -1
          #    currentLoc = demoMap[x][y]
        else: 
             print('Try again!')
        
        if canMove == True and valueHold != 0 and moveTile[currentLoc]['dir'] == 'right':
             if moveTile[currentLoc]['jump'] == True:
                  y += valueHold
                  currentLoc = demoMap[y][x]
                  canMove = False
             else:
                  x += valueHold
                  currentLoc = demoMap[y][x]
       
        if canMove == True and valueHold != 0 and moveTile[currentLoc]['dir'] == 'left':
             if moveTile[currentLoc]['jump'] == True:
                  y += valueHold
                  currentLoc = demoMap[y][x]
                  canMove = False
             else:
                  x -= valueHold
                  currentLoc = demoMap[y][x]
        
        if moveTile[currentLoc]['t'] == '#':
             x, y= 0, 0
             currentLoc = demoMap[x][y]

                  
          #    if valueHold == 0:
          #         currentLoc = demoMap[x][y]

        input("#: Enter to Continue!")
        print(x_len, y_len)
        
        
    if choice == "0":
          quit()
