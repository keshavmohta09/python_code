alpha = input("Enter letter : ")
n = 0
while n<=5:
    n = int(input("Enter the size of alphabet > 5 : "))

if alpha in 'Aa':
    for i in range(1,n+1):
        for j in range(i,n+1):
            print(end=' ')
        for j in range(1,i+1):
            if j in (1,i) or i == n//2+1:
                print('a',end=' ')
            else:
                print(end='  ')
        print()

elif alpha in 'Cc':
    for i in range(n):
        if i == 0:
            print(end='  ')
        else:
            print('c', end=' ')
    print()
    for i in range(n-1):
        print('c')
    for i in range(n):
        if i==0:
            print(end='  ')
        else:
            print('c',end=' ')

elif alpha in 'Ii':
    for i in range(n):
        print('     i')

elif alpha in 'Zz':
    for i in range(n):
        print(' z',end='')
    print()
    for i in range(1,n-1):
        for j in range(i,n):
            print(end='  ')
        print('z')
    for i in range(n):
        print(' z',end='')