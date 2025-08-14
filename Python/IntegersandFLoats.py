'''Integers and Floats
-Basics'''

#1 storing my age in variable and printing it
age=21
print(age)

#2 storing the float value price in varraible and printing it
price=2000.25
print(price)

#3  adding,subtracting,multiplying,dividing two integers and also printing there data type
a=5
b=4
add=(a+b)
print(add)
print(type(add))
sub=(a-b)
print(sub)
print(type(sub)) 
multi=(a*b)
print(multi)
print(type(multi))
div=(a/b)
print(type(div))


#4 dividing two integers and showing normal divison, floor division and modulus
normal_div=(a/b)
print(normal_div)
print(type(normal_div))
floor_div=(a//b)
print(floor_div)
print(type(floor_div))
modulus=(a%b)
print(modulus)
print(type(modulus))

#5 multiplying a float and integer and printing its results
c=(5)
d=(4.5)
e=(c*d)
print(e)
print(type(e))

'''Level 2 - Operators'''


import math
celcius=float(input("Enter the celcius:"))
farenhiet=(celcius*9/5) + 32
farenhiet=(f"Converting C to F:{farenhiet}")
print(farenhiet)


circle=float(input("Enter the radius:"))
Area=math.pi * circle**2
Area=(f"Area of circle:{Area}")
print(Area)
Circum=(2*math.pi *circle)
Circum=(f"Circumference of circle:{Circum}")
print(Circum)


#absolute
num1=-10
num2=-5
num3=abs(num1)-abs(num2)
print(num3)

#round up
print(round(3.14159))
print(round(3.14159,2))

#floor division
w=input("Enter first number:")
x=input("Enter second number:")
y=(w//x)
print(y)












