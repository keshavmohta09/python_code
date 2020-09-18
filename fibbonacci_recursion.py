def fibbonacci_r(n):
    global temp1
    global temp2
    add = temp1+temp2
    if add<=n:
        print(add,end=' ')
        temp1 = temp2
        temp2 = add
        return fibbonacci_r(n)


temp1, temp2 = -1, 1
n = int(input("Enter the last number of series: "))
print("\nFibbonacci series is 0 to",n,":- ")
fibbonacci_r(n)
print()