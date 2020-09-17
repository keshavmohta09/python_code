from random import randint
num = input("Press any key for toss: ")
while True:
    if True:
        r = randint(1, 2)
        print("Head" if r==1 else "Tails")
    opt = input("for toss again press r else press any key: ")
    if opt != 'r':
        exit()