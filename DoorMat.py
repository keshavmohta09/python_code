'''Size: 7 x 21
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
'''
from time import sleep
while True:
    m = int(input("Enter the odd value of m : "))
    if m%2!=0:
        break
n = 3*m
t = 1
print('\nProcessing..........\n')
sleep(1)
for i in range(1,m+1):
    sleep(.05)
    if i<(m+1)//2:
        q = '.|.'*t
        t+=2
        print(q.center(n,'-'))
    elif i==(m+1)//2:
        print('WELCOME'.center(n,'-'))
    else:
        t-=2
        q='.|.'*t
        print(q.center(n,'-'))