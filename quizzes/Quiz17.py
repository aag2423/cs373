#!/usr/bin/env python3

"""
CS373: Quiz #17 (5 pts) <Prateek>
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following?
    (4 pts)

True
True
False
False
"""

from copy import copy, deepcopy

class A :
    def __init__ (self) :
        self.a = [2, [3], 4]

x = A()
y = copy(x)

print(x.a    is y.a)
print(x.a[1] is y.a[1])

z = deepcopy(x)

print(x.a    is z.a)
print(x.a[1] is z.a[1])
