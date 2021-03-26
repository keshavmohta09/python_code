l = [int(input("Enter data : ")) for i in range(int(input("Enter the number of elements : ")))]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[j],l[i] = l[i],l[j]
print(l)