#!/usr/bin/env python3

"""
CS373: Quiz #20 (5 pts) <Jake>
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following?
    (2 pts)

[4, 2, 3]
"""

a = [2, 3, 4]
print((a + a)[10:-10:-2])

""" ----------------------------------------------------------------------
 2. What is the output of the following?
    Alternatively, indicate that it's an error.
    (2 pts)

2
AttributeError: 'B' object has no attribute 'i'
3
"""

class A :
    def __init__ (self) :
        self.i = 2

    def f (self) :
        print(self.i)

class B (A) :
    def __init__ (self) :
        pass

    def g (self) :
        self.i = 3

x = A()
x.f()

x = B()
#x.f()

x.g()
x.f()
