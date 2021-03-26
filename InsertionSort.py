l = [int(input("Enter data : ")) for i in range(int(input("Enter the number of elements : ")))]
for i in range(1,len(l)):
    j = i-1
    while j>=0 and l[j+1]<l[j]:
        l[j+1], l[j] = l[j], l[j+1]
        j-=1
print(l)