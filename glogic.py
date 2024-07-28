# finding the game logic here
# players play each turn roll dice then move their character

# elist = ['a', 'b', 'c']

# for item in range(3):
#     if item != 2:
#         ehold = elist[item]
#         elist[item] = elist[item+1]
#         print(item)
#     else:
#         elist[item] = 'a'

# print(elist)

demoMap = [
    ['a', 'b', 'c'],
    ['1', '2', '3']
]

for row in range( 2): # x 
        # print(row)
        for col in range( 3): # y
            # print(row)
            print(demoMap[row][col], end = ' ')
        print(' ')