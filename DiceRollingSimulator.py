from random import randint
while True:
    r = randint(1,6)
    if r==1:
       print("|     |")
       print("|  0  |")
       print("|     |")
    elif r==2:
       print("|0    |")
       print("|     |")
       print("|    0|")
    elif r==3:
       print("|0    |")
       print("|  0  |")
       print("|    0|")
    elif r==4:
       print("|0   0|")
       print("|     |")
       print("|0   0|")
    elif r==5:
       print("|0   0|")
       print("|  0  |")
       print("|0   0|")
    else:
       print("|0   0|")
       print("|0   0|")
       print("|0   0|")
    cont = input("press Enter to roll again else press any key to exit: ")
    if cont != '':
        exit()