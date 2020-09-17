def area_of_circle(r):
    if r<0:
        return None
    else:
        return 3.14*r**2
radius = int(input("Enter the radius of circle: "))
area = area_of_circle(radius)
print("Area of circle = ",area)