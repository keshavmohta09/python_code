year=int(input("Enter the year: "))
if year%100==0 and year%400==0:
    print("It is a leap year")
elif year%4==0:
    print("It is a leap year")
else:
    print("It is not leap year")