n = int(input("Enter the value of n>1 : "))
allnum = [i for i in range(2,n+1)]
temp = len(allnum)+1
j = 0
k = 1
while True:
    j+=1
    k+=1
    while True:
        if k not in allnum and k!=temp:
            k+=1
        else:
            break
    if k==temp:
        break
    for i in allnum[j:]:
        if i%k==0:
            allnum.remove(i)
print(allnum)