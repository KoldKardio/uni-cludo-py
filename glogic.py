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
currentLoc = demoMap[x][y]

tile_name = moveTile[currentLoc]['t']



# dice check
def diceRoll():
    return random.randint(1, 6)
# print(diceRoll())


# gameLoop
while True:
    os.system('cls')
    mapDraw()
    # check
    print(currentLoc)
    # check
    #  get input
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
