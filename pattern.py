n = int(input("Enter the greatest no. of * in a line: "))
i=n
for i in range(1,n+1):
    temp = 1
    while temp<=i:
        print("*",end=' ')
        temp+=1
    print()
for i in range(n-1,0,-1):
    temp = 1
    while temp<=i:
        print("*",end=' ')
        temp+=1
    print()