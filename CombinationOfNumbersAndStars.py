'''1 * 2 * 3 * 4
   1 * 2 * 3
   1 * 2
   1'''

n = int(input("Enter the maximum number of pattern : "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
        if j<i:
            print('*',end=' ')
    print()