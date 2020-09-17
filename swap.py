first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
print("\nBefore swapping fist number is",first,"and second number is",second)
first = first + second
second = first - second
first = first - second
print("\nAfter swapping first number is",first,"and second number is",second)