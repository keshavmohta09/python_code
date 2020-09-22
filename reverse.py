num = int(input("Enter the number: "))
temp = num
rev = 0
while num!=0:
    mod = num%10
    num//=10
    rev = rev*10+mod
print("The reverse number of %d is %d"%(temp,rev))