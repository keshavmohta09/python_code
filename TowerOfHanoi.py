def TOH(n,S,D,A):
    if n==1:
        print(f"Move disk 1 from {S} to {D}")
        return
    TOH(n-1,S,A,D)
    print(f'Move disk {n} from {S} to {D}')
    TOH(n-1,A,D,S)
n = int(input('Number of disks : '))
TOH(n,'A','C','B')
print('Total number of moves :',2**n-1)