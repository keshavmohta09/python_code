num1 = int(input('Enter num1: '))
num2 = int(input("Enter num2: "))
temp = int(input("for (num1/num2) press 1: \nfor (num2/num1) press 2:\n "))

if(temp == 1):
    value = input("Output in the form of int or float: ")
    if(value == "int"):
        num3 = num1//num2
        print("The integer form of divison is: ",num3)
        print("\n")
    elif(value == "float"):
        num3 = num1/num2
        print("The float form of divison is :",num3)
        print("\n")
    else:
        print("Enter correct form of number\n")

elif(temp == 2):
    value = input("Output in the form of int or float: ")
    if(value == "int"):
        num3 = num2//num1
        print("The integer form of divison is: ",num3)
        print("\n")
    elif(value == "float"):
        num3 = num2/num1
        print("The float form of divison is :",num3)
        print("\n")
    else:
        print("Enter correct form of number\n")

else:
    print("Enter the corret information\n")