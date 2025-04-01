# Dominic Meikle
# 2/27/25
# P2Lab1
# This program calculates the diameter, circumference, and area using a radius given by the user.

import math
pi = math.pi

#get radius
r = float(input("What is the radius of the circle? "))

#calculate diameter, area, and circumference
d = r*2
a = pi*r**2
c = 2*pi*r

#print values
print(f"The diameter of the circle is {d:.1f}")
print(f"The circumference of the circle is {c:.2f}")
print(f"The area of the circle is {a:.3f}")