n = int(input('Enter the number of elements : '))
t = (input(f"Enter element no. {i+1} : ") for i in range(n))
t = sorted(t)
search = input('Enter the element for search : ')
temp = len(t)//2
if search<=t[temp]:
    for i in range(temp+1):
        if t[i]==search:
            print('Element present in given list')
            exit()
else:
    for i in range(temp,len(t)):
        if t[i]==search:
            print('Element is present in given list')
            exit()
print('Element is not present in given list')