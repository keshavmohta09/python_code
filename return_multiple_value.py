def sum_subtraction(a,b):
    return a+b,a-b
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
result = sum_subtraction(first,second)
print("Sum and Subtraction: ",result)