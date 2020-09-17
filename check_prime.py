num = int(input("Enter a number: "))
i = 2
if num==2:
    print(num,"is a prime number")
elif num<2:
    print(num,"is not a prime number")
else:
    while i<num:
        if num%i==0:
            print(num,"is not a prime number")
            break
        else:
            i+=1
    else:
        print(num,"is a prime number")