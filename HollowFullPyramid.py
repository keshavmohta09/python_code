'''
size : 6
     *
    * *
   *   *
  *     *
 *       *
* * * * * *
'''
n = int(input("Enter the size of the pyramid : "))
for i in range(1,n+1):
    for j in range(i,n):
        print(end=' ')
    for j in range(1,i+1):
        if j in (1,i) or i==n:
            print('*',end=' ')
        else:
            print(end='  ')
    print()