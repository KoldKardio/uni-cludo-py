from colorama import init, Fore

init()

x = Fore.RED + 'c'
dColl = ['a', 'b', Fore.RED +'x']

for item in dColl:
    print( Fore.YELLOW + item)
