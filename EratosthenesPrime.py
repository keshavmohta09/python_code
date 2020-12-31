def EratosthenesPrime(n):
    prime_list = [i for i in range(2,n+1)]
    for i in prime_list:
        for j in prime_list:
            if( i!=j and j%i==0):
                prime_list.remove(j)
    return prime_list

n = int(input("Enter the value of n(>1) : "))
print(EratosthenesPrime(n))