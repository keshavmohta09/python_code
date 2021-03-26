def binary_search(l_list,key,l,h):
    while l<=h:
        m = l+(h-l)//2
        if l_list[m]==key:
            print(key,'present in',m,'position.')
            return True
        elif l_list[m]>key:
            h = m-1
        else:
            l = m+1
    else:
        return False

l_list = [int(input('Enter data : ')) for i in range(int(input('Enter the number of elements : ')))]
key = int(input('Enter the number to search : '))
l_list.sort()
l = 0
h = len(l_list)-1
r = binary_search(l_list,key,l,h)
if not r:
    print('Element is not present in list')