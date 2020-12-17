import numpy as np

def creatematrix(r,c):
    l = []
    for i in range(r):
        for j in range(c):
            l.append(int(input(f"Enter a{i + 1}{j + 1} : ")))
        print()
    return np.array(l).reshape(r,c)

def multiplymatrix(arr1,arr2):
    m, n = arr1.shape
    n, o = arr2.shape
    l = []
    for i in range(m):
        for j in range(o):
            temp = 0
            for k in range(n):
                temp += arr1[i][k]*arr2[k][j]
            l.append(temp)
    return np.array(l).reshape(m,o)

if __name__=='__main__':
    m = int(input("Enter the no. of rows of 1st matrix : "))
    n = int(input("Enter the no. of columns of 1st matrix or no. of rows of 2nd matrix : "))
    arr1 = creatematrix(m,n)
    o = int(input("Enter the no. of columns of 2nd matrix : "))
    arr2 = creatematrix(n,o)
    arr = multiplymatrix(arr1,arr2)
    print(arr)