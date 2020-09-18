num = int(input("Enter the number: "))
fact = 1
print(num,end='')
while num!=0:
    fact*=num
    num-=1
print("! =",fact)