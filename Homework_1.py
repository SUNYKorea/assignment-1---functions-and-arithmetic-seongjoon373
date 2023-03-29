# Name:Seong Jonn Kim
# SBUID: 115504349

# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit): 
   #fahrenheit=input("Give any number: ")
   fahrenheit=int(fahrenheit)
   celsius=(5/9)*(fahrenheit-32)
   return celsius

def what_to_wear(celsius):
   if celsius<-10:
       print("Puffy jacket")
   elif 0>=celsius>=-10:
       print("Scarf")
   elif 10>=celsius>0:
       print("Sweater")
   elif 20>=celsius>10:
       print("Light jacket")
   else:
       print("T-shirt")

# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    #x1=input("Enter x1 value:")
    x1=int(x1)
    #y1=input("Enter y1 value:")
    y1=int(y1)
    #x2=input("Enter x2 value:")
    x2=int(x2)
    #y2=input("Enter y2 value:")
    y2=int(y2)
    #x3=input("Enter x3 value:")
    x3=int(x3)
    #y3=input("Enter y3 value:")
    y3=int(y3)
    area=abs(((x1*y2+x2*y3+x3*y1)-(x1*y3+x2*y1+x3*y2))/2)
    return area




def euclidean_distance(x1, y1, x2, y2):
    d=((x1-x2)**2+(y1-y2)**2)**0.5
    return d

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    perimeter=euclidean_distance(x1, y1,x2,y2)+euclidean_distance(x2, y2,x3,y3)+euclidean_distance(x3, y3,x1,y1)
    print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )


# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 

def deg2rad(deg):
    number_sides=input("Enter the value of number sides:")
    #number_sides = 4
    number_sides=int(number_sides)
    deg=180/number_sides
    import math
    valueofpi=math.pi
    rad=(valueofpi/180*deg)
    return rad

def apothem(number_sides, length_side):
    length_side=input("Enter the value of length side:")
    #length_side = 4
    length_side=int(length_side)
    import math
    valueoftangent=math.tan(deg2rad(number_sides))
    a=number_sides/(2*valueoftangent)
    return a

def polygon_area(number_sides, length_side):
    polygon_area=(number_sides*length_side*apothem(number_sides, length_side))/2
    return polygon_area


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = 1, 3, 5, 2, 4, 6 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 4
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))
