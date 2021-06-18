'''
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
'''

n = int(input("Enter the size : "))
for i in range(1,n+1):
    temp = 96 + n
    s = ''
    for j in range(1,i+1):
        s+=chr(temp)+'-'
        temp-=1
    temp+=1
    for j in range(1,i):
        temp+=1
        s+=chr(temp)+'-'
    s = s[:-1]
    s = s.center(4*n-3,'-')
    print(s)

for i in range(n,1,-1):
    temp = 96 + n
    s = ''
    for j in range(i,1,-1):
        s+=chr(temp)+'-'
        temp-=1
    temp+=1
    for j in range(i,2,-1):
        temp+=1
        s+=chr(temp)+'-'
    s = s[:-1]
    s = s.center(4*n-3,'-')
    print(s)