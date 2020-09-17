num = int(input("Enter the number: "))
temp_num = num
fact = 1
while num!=0:
    fact*=num
    num-=1
print("Factorial of the",temp_num,"is",fact)