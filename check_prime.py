from datetime import datetime
num = int(input("Enter a number: "))
s = datetime.now()
i = 2
if num==2:
    print(num,"is a prime number.")
elif num<2:
    print(num,"is not a prime number.")
else:
    while i<num//2:
        if num%i==0:
            print(num,"is not a prime number.")
            break
        else:
            i+=1
    else:
        print(num,"is a prime number.")
e = datetime.now()
print(f"Total time taken : {(e-s).total_seconds()} seconds.")