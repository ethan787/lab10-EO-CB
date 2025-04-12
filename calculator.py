"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b): 
    return a +b
def subtract(a, b):
    return a -b
def multiply(a, b):
    return a * b
def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a
def logarithm(a, b):
    #we're supposed to raise a valueerror for something here?
    return math.log(a, b)
def exponent(a, b):
    return a ** b



