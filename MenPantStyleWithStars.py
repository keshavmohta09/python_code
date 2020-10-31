'''**********
   ****__****
   ***____***
   **______**
   *________*'''
n = int(input("Enter the number of lines : "))
for i in range(n):
    for j in range(n):
        print('*',end='')
    for j in range(i):
        print('__',end='')
    for j in range(n):
        print('*',end='')
    n-=1
    print()