num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))
temp = int(input("for (num1-num2) press 1: \nfor (num2-num1) press 2:\n "))
if(temp == 1):
    print("The difference of these numbers is ",num1-num2)
elif(temp == 2):
    print("The difference of these numbers is ",num2-num1)
else:
    print("Enter correct information")
