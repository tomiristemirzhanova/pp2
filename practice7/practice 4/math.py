#1. Write a Python program to convert degree to radian.

import math 

degree=float(input("Input degree: "))
radian = degree * (math.pi/180)

print ("Output radian: ", radian)

#2. Write a Python program to calculate the area of a trapezoid.

height = float(input("Height: "))
b1 = float(input("Base, first value: "))
b2 = float(input("Base, second value: "))

area = 0.5 * (b1 + b2) * height

print("Expected Output:", area)

#3. Write a Python program to calculate the area of regular polygon.

import math 
n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

area = (n * s * s) / (4 * math.tan(math.pi / n))

print("The area of the polygon is:", round(area, 0))

# 4. Write a Python program to calculate the area of a parallelogram.
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height

print("Expected Output:", area)