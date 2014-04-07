#!/usr/bin/env python3

"""
CS373: Quiz #30 (5 pts) <Jake>
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following program?
    (4 pts)

A.A() A.A() False
A.A() True
True
"""

def Decorator (c) :
    x = c()
    return lambda : x

class A (object) :
    def __init__ (self) :
        print("A.A()", end = " ")

print(A() is A())

A = Decorator(A)
print(A() is A())

A = Decorator(A)
print(A() is A())
