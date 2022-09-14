import math

#the length of a side
from math import sin, pi, sqrt

r = float(input("Input r = "))
s = 2*r*sin(math.pi/5)

#computing the area of a pentagon
Area=(3*sqrt(3)/2)*s**2
print("Pentagon area = ",Area) 
