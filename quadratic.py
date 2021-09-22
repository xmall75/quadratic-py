#!/usr/bin/env
# Quadratic Equations Solver (complex number included)
# credits Izzul, Dida, Rep
# ax^2 + bx + c
# input a, b, and c

import math
import cmath

a, b, c = input("Input a, b, c (example: 1 5 4): ").split()
a = int(a)
b = int(b)
c = int(c)

d = b**2 - 4*a*c
if d > 0:
    x1 = ((-b + math.sqrt(d))/(2*a))
    x2 = ((-b - math.sqrt(d))/(2*a))
    print("x1, x2 : ", f'{x1:.2f}' + ", " f'{x2:.2f}')
elif d < 0:
    x1 = ((-b + complex(0, math.sqrt(d*(-1))))/(2*a))
    x2 = ((-b - complex(0, math.sqrt(d*(-1))))/(2*a))
    print("x1 :", f'{x1.real:.2f}' + "+" + f'{x1.imag:.2f}' + "i", "\nx2 :", f'{x2.real:.2f}' + f'{x2.imag:.2f}' + "i")
else:
    x1 = ((-b + math.sqrt(d))/(2*a))
    x2 = ((-b - math.sqrt(d))/(2*a))
    if x1 == x2:
        print("x : ", f'{x1:.2f}')