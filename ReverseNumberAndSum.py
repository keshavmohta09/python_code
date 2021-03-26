inp = input("Enter the number : ")
rev, sum = '', 0
for i in range(len(inp)-1,-1,-1):
    rev+=inp[i]
    sum+=int(inp[i])
print(f'Reverse of {inp} = {rev}\nSum of {inp} = {sum}')