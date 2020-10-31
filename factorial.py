num = int(input("Enter the number : "))
if num<0:
    print("factorial not defined for negative values.")
    exit()
fact = 1
for i in range(1,num+1):
    fact*=i
print(f"{num}! = {fact}")
import math as m
print(m.factorial(-5))