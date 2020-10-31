'''5 5 5 5 5
   4 5 5 5 5
   3 4 5 5 5
   2 3 4 5 5
   1 2 3 4 5'''

n = int(input("Enter the value of n : "))
for i in range(1,n+1):
    q = n+1-i
    for j in range(i-1):
        print(q,end=' ')
        q+=1
    for j in range(n+1-i):
        print(n,end=' ')
    print()