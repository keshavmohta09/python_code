num = int(input("Enter the number: "))
temp_num = num
rev = 0
while num!=0:
    temp = num%10
    num//=10
    rev = rev*10+temp
print("The reverse number of",temp_num,"is",rev)