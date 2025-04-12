#https://github.com/ethan787/lab10-EO-CB
#Partner 1: Christen Borrero
#Partner 2: Ethan Ortiz
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b):
    return a + b
def mul(a,b):
    return a*b
def div(a,b):
    if a ==  0:
        raise ZeroDivisionError
    return b/a
def exp(a,b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)
def hypotenuse(a, b):
    sum = (a**2) + (b**2)
    return square_root(sum)
def add(a, b): 
    return a +b
def subtract(a, b):
    return a -b
def logarithm(a, b):
    #we're supposed to raise a valueerror for something here?
    return math.log(a, b)



