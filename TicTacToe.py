print("\n**********Welcome to Tic Tac Toe Game**********\n\n")
player1 = input("Enter the name of player 1: ")
player2 = input("Enter the name of player 2: ")
place = [' ']*10 #to print pattern
check_choice = [0]*10                             #to check already exist input
temp_count = 1                                    #for all 9 choices
local = 0                                         #to declaring result
count_choice = 1                                  #to fill the check_choice list
print()

def func_for_player1():
    '''This function for player1's choice checking for enter the same number and enter the other number except 1 to 9'''
    global choice1
    print("\nEnter the choice of", player1, end=': ')
    choice1 = int(input())
    if choice1>9 or choice1<1:
        print("This number is not valid")
        again_for_player1()
    if choice1>=1 and choice1<=9:
        for i in range(1, 10):
            if check_choice[i] == choice1:
                print("This number is already used")
                again_for_player1()

def again_for_player1():
    '''The use of this function is to repeat the func_for_player1() function.'''
    func_for_player1()

def func_for_player2():
    '''This function for player2's choice checking for enter the same number and enter the other number except 1 to 9'''
    global choice2
    print("\nEnter the choice of", player2, end=': ')
    choice2 = int(input())
    if choice2>9 or choice2<1:
        print("This number is not valid")
        again_for_player2()
    if choice2>=1 and choice2<=9:
        for i in range(1,10):
            if check_choice[i]==choice2:
                print("This number is already used")
                again_for_player2()

def again_for_player2():
    '''The use of this function is to repeat the func_for_player2() function.'''
    func_for_player2()


for i in range(1,10):
    print(' ',i,end='')
    if i==1 or i==2 or i==4 or i==5 or i==7 or i==8:
        print("  | ",end='')
    if i==3 or i==6:
        print("\n-------------------")
print("\n\nPress any number for each place\n",player1,"'s choice is X\n",player2,"'s choice is O\n")
while temp_count<10:
    func_for_player1()
    check_choice[count_choice] = choice1
    count_choice+=1
    print()
    for i in range(1,10):
        if choice1==i:
            place[i]='X'
        print(' ',place[i],end='')
        if i == 1 or i == 2 or i == 4 or i == 5 or i == 7 or i == 8:
                print("  | ", end='')
        if i == 3 or i == 6:
                print("\n-------------------")
    print()
    temp_count+=1
    if (place[1] == place[2] == place[3] == 'X') or \
        (place[4] == place[5] == place[6] == 'X') or \
        (place[7] == place[8] == place[9] == 'X') or \
        (place[1] == place[4] == place[7] == 'X') or \
        (place[2] == place[5] == place[8] == 'X') or \
        (place[3] == place[6] == place[9] == 'X') or \
        (place[1] == place[5] == place[9] == 'X') or \
        (place[3] == place[5] == place[7] == 'X'):
        print('\n',player1,'win\n')
        local+=1
        break
    if temp_count<9:
        func_for_player2()
        check_choice[count_choice] = choice2
        count_choice+=1
        print()
        for i in range(1,10):
            if choice2 == i:
                place[i] = 'O'
            print(' ', place[i], end='')
            if i == 1 or i == 2 or i == 4 or i == 5 or i == 7 or i == 8:
                print("  | ", end='')
            if i == 3 or i == 6:
                print("\n-------------------")
        print()
        temp_count += 1
        if (place[1] == place[2] == place[3] == 'O') or \
            (place[4] == place[5] == place[6] == 'O') or \
            (place[7] == place[8] == place[9] == 'O') or \
            (place[1] == place[4] == place[7] == 'O') or \
            (place[2] == place[5] == place[8] == 'O') or \
            (place[3] == place[6] == place[9] == 'O') or \
            (place[1] == place[5] == place[9] == 'O') or \
            (place[3] == place[5] == place[7] == 'O'):
            print('\n',player2, 'win')
            local+=1
            break
if local==0:
    print('\n',"Draw")