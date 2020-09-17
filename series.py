def fact(n):
    if n==1:    return 1
    else:   return n * fact(n-1)

while True:
    temp = 1
    n = int(input("Enter the last number of series: "))
    for i in range(1,n+1):
        temp+=(1/fact(i))
    if n>2:
        print("1 + 1/1! + __ + 1/",n,"! = ",temp)
        break
    elif n==1:
        print("1 + 1/1! = ", temp)
        break
    elif n==2:
        print("1 + 1/1! + 1/2! = ", temp)
        break
    else:
        print("\nEnter the value which is greater than zero\n")
