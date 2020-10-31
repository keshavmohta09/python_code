'''5 4 3 2 1 1 2 3 4 5
   5 4 3 2     2 3 4 5
   5 4 3         3 4 5
   5 4             4 5
   5                 5'''
n = int(input("Enter the maximum number of pattern : "))
q = 0
for i in range(n):
    for j in range(n,q,-1):
        print(j,end=' ')
    for j in range(i):
        print('   ',end=' ')
    for j in range(q+1,n+1):
        print(j,end=' ')
    print()
    q+=1