import random, os

# game logic part 2: using simple method for data transmission
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

# dice check
def diceRoll():
    return random.randint(1, 6)

# coordinates
x, y= 0, 0
y_len = len(demoMap)-1
x_len = len(demoMap[0])-1
currentLoc = demoMap[x][y]

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

        if valueHold == 1:
             print('Your player can move.')
        else: print('Try again!')

        input("#: Enter to Continue!")
        
        
    if choice == "0":
          quit()
