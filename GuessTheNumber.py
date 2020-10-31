from random import randint
rand_num = randint(1,100)
guess = temp = 8
print("You have",guess,"guesses")
for number in range(0,temp):
    num = int(input("Guess the value: "))
    if num==rand_num and guess>0:
        print("\n**********You win**********")
        break
    elif num!=rand_num and guess>1:
        guess -= 1
        if num<rand_num:
            print("\nIncrease the value")
            print("\nNow you have",guess,"guess")
            continue
        else:
            print("\nDecrease the value")
            print("\nNow you have", guess, "guess")
            continue
    else:
        print("\n**********Game Over**********")
        print("The secret value is",rand_num)