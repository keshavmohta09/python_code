from random import randint
while True:
    r = randint(1,6)
    print('┌-----┐')
    if r==1:
       print("|     |")
       print("|  ●  |")
       print("|     |")
    elif r==2:
       print("|●    |")
       print("|     |")
       print("|    ●|")
    elif r==3:
       print("|●    |")
       print("|  ●  |")
       print("|    ●|")
    elif r==4:
       print("|●   ●|")
       print("|     |")
       print("|●   ●|")
    elif r==5:
       print("|●   ●|")
       print("|  ●  |")
       print("|●   ●|")
    else:
       print("|●   ●|")
       print("|●   ●|")
       print("|●   ●|")
    print('└-----┘')
    cont = input("press Enter to roll again else press any key to exit: ")
    if cont != '':
        exit()