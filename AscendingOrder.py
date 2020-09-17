n = int(input("Enter how many numbers you want to add: "))
list_l = []
print("Enter the numbers: ")
for number in range(0,n):
    num = int(input())
    list_l.append(num)
list_l.sort()
print(list_l)