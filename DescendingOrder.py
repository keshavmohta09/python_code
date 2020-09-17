n = int(input("Enter how many numbers you want to add: "))
list_l = []
print("Enter the numbers: ")
for number in range(n):
    num = input()
    try:
        num = int(num)
    except:
        num = float(num)
    list_l.append(num)
list_l.sort()
list_l.reverse()
print(list_l)