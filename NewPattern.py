'''1 10 11 20 21
   2 9 12 19 22
   3 8 13 18 23
   4 7 14 17 24
   5 6 15 16 25'''
l = [i+1 for i in range(25)]
k = []
oddeven = 2
for i in range(0,26,5):
    a = l[i:i+5]
    if oddeven%2!=0:
        a.reverse()
    k.append(a)
    oddeven+=1
k.pop()
for i in range(5):
    a = []
    for j in range(5):
        a.append(k[j][i])
    for item in a:
        print(item,end=' ')
    print()
