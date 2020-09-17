def factorial_custom(num):
    if num==1:
        return 1
    else:
        return num*factorial_custom(num-1)

def additon(a,b):
    return a+b

def substraction(a,b):
    return a-b

def division_int(a,b):
    return a//b

def division_float(a,b):
    return a/b

def reverse_int(num):
    rev = 0
    while num != 0:
        temp = num % 10
        num //= 10
        rev = rev * 10 + temp
    return rev