"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b):
    return a + b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if a ==  0:
        raise ZeroDivisionError
    return b/a
def log(a,b):
    return math.log(a,b)
def exp(a,b):
import math

def add(a, b): 
    return a +b
def subtract(a, b):
    return a -b
def multiply(a, b):
    return a * b

def logarithm(a, b):
    #we're supposed to raise a valueerror for something here?
    return math.log(a, b)
def exponent(a, b):
    return a ** b



