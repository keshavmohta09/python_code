# def fibbonacci_r(n):
#     global temp1
#     global temp2
#     add = temp1+temp2
#     if add<=n:
#         print(add,end=' ')
#         temp1 = temp2
#         temp2 = add
#         return fibbonacci_r(n)
#
#
# temp1, temp2 = -1, 1
# n = int(input("Enter the last number of series: "))
# print("\nFibbonacci series is 0 to",n,":- ")
# fibbonacci_r(n)
# print()

def fibonacci_recursion(n):
    if n<=1:
        return n
    return (fibonacci_recursion(n-1)+fibonacci_recursion(n-2))
n = int(input('Enter the number of elements : '))
if n<=0:
    print(0)
else:
    for i in range(n):
        print(fibonacci_recursion(i))