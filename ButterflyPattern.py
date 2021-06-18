'''
size : 5
*               *
* *           * *
* * *       * * *
* * * *   * * * *
* * * * * * * * *
* * * * * * * * *
* * * *   * * * *
* * *       * * *
* *           * *
*               *
'''

n = int(input("Enter the size of the pattern : "))
temp = 4*n
l = []
for i in range(1,n+1):
    temp -= 4
    s = ''
    for j in range(i):
        s+='* '
    s = s.ljust(temp+len(s),' ')+s
    print(s)
    l.append(s)
for i in range(len(l)-1,-1,-1):
    print(l[i])