# def hcf (a,b):
#     if a>b:
#         small=b
#     else:
#         small=a
#     mul = 1
#     i = 2
#     print(f'\nHCF of {a} and {b} : \nFactors : ')
#     while i<=small:
#         if (a%i==0) and (b%i==0):
#             print(i)
#             mul*=i
#             a = a//i
#             b = b//i
#         else:
#             i+=1
#     return "Result : "+str(mul)
# print(hcf(int(input("Enter the first number : ")),int(input("Enter the second number : "))))

def h_cf(a,b):
    if a>b:
        small=b
    else:
        small=a
    fac=1
    for i in range(1,small+1):
        print(i)
        if i==1:
            i=2
        if(a%i==0) and(b%i==0):
            fac*=i
            a=a//i
            b=b//i
            i = 0
            print(i)

    print(fac)
h_cf(24,40)#logic kahee break ho raha h???>>>>>>>?????