while True:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the last number: "))
    if num1>num2 or num1<1:
        print("Enter the correct numbers")
        continue
    for i in range(num1,num2+1):
        for j in range(2,i//2+1):
            if i%j == 0:
                break
        else:   print(i,end=' ')
    exit('\n')