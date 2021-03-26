# l = [i for i in range(2,int(input("Enter the value of n>2 : "))+1)]
# print(l)
# c = 0
# for i in l:
#     l = list(filter(lambda x : (x%i!=0) or (x==i), l))
#     c+=1
# print(l,c)







l = [i for i in range(2,int(input("Enter the value of n>2 : "))+1)]
c = 0
len_l = len(l)
for _ in range(len_l):
    try:
        i = l[_]
        l = list(filter(lambda x: (x % i != 0) or (x == i), l))
        c += 1
    except:
        break
print(l,c)







# Python program to print all primes smaller than or equal to 
# n using Sieve of Eratosthenes 
  
# def SieveOfEratosthenes(n): 
      
#     # Create a boolean array "prime[0..n]" and initialize 
#     # all entries it as true. A value in prime[i] will 
#     # finally be false if i is Not a prime, else true. 
#     prime = [True for i in range(n + 1)] 
#     p = 2
#     while (p * p <= n): 
          
#         # If prime[p] is not changed, then it is a prime 
#         if (prime[p] == True): 
              
#             # Update all multiples of p 
#             for i in range(p * 2, n + 1, p): 
#                 prime[i] = False
#         p += 1
#     prime[0]= False
#     prime[1]= False
#     # Print all prime numbers 
#     for p in range(n + 1): 
#         if prime[p]: 
#             print(p) #Use print(p) for python 3 
  
# # driver program 
# if __name__=='__main__': 
#     n = 30
#     print("Following are the prime numbers smaller")  
#     #Use print("Following are the prime numbers smaller") for Python 3 
#     print ("than or equal to", n )
#     #Use print("than or equal to", n) for Python 3 
#     SieveOfEratosthenes(n) 