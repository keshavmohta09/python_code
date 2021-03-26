l = [1,1,1,1,1,2,2,3,8,8,8,8]
d = {}
l1 = list(map(str,l))
l1 = ''.join(l1)
q = []
for i in set(l):
    temp = l1.count(str(i))
    d[i] = temp
    q.append(temp)
print(d)
q.sort(reverse=True)
l = []
for i in q:
    for j in d.keys():
        if (d[j]==i) and (j not in l):
            l.append(j)
print(l)