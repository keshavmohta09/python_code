num = int(input("Enter the number: "))
temp_num = num
add = 0
while num!=0:
    temp = num%10
    add = add+temp
    num//=10
print("The sum of digits of the",temp_num, "is",add)