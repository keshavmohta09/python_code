'''Size: 7 x 21
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
'''
while True:
    m = int(input("Enter the odd value of m : "))
    if m%2!=0:
        break
n = 3*m
t = 1
for i in range(1,m+1):
    if i<(m+1)//2:
        q = 3*t
        t+=2
        for j in range((n-q)//2):
            print('-',end='')
        dsgn = 1
        while(dsgn<q):
            print('./.',end='')
            dsgn+=3
        for j in range((n-q)//2):
            print('-',end='')
        print()
    elif i==(m+1)//2:
        for i in range((n-7)//2):
            print('-',end='')
        print('WELCOME',end='')
        for i in range((n-7)//2):
            print('-',end='')
        print()
    else:
        t-=2
        q=3*t
        for j in range((n-q)//2):
            print('-',end='')
        dsgn = 1
        while (dsgn<q):
            print('./.',end='')
            dsgn += 3
        for j in range((n-q)//2):
            print('-',end='')
        print()