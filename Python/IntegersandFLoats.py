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
# y=(w//x)
print(y)

#Type casting & built ins
u=20
v=float(u)
print(v)

#converting string into float
red="25.5"
green=float(red)
print(green +10)

#finding min and max element of a list and sum
large=[20,30,35]
min_large=min(large)
print(min_large)
max_large=max(large)
print(max_large)
add=sum(large)
print(add)

#using random to print random number from 1 to 100 (using python standard library)
import random
one=random.randint(1,100)
print(f"Random number betweeen 1 to 100:{one}")

'''challenge problems'''
#1 checking if the number is even or odd
check=float(input("Enter a number:"))
if check/2:
    print(check,"Is even")
else:
    print(check,"is odd")

#2
import math

principle=3000
rate=4/100
time=4
ci=principle*(1+rate/time)**(time)
print(ci)

#converting seconds into hour,minute and second format
second=300000
minutes=second/60
hours=minutes/60














