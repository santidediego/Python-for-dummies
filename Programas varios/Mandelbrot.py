#! /usr/bin/python3

import math
 
def mandelbrot(z , c , n=40):
    if abs(z) > 1000:
        return float("nan")
    elif n > 0:
        return mandelbrot(z ** 2 + c, c, n - 1) 
    else:
        return z ** 2 + c
