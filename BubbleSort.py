l = [int(input("Enter data : ")) for i in range(int(input("Enter the number of elements : ")))]
for i in range(len(l)-1):
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
print(l)