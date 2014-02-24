#!/usr/bin/env python3

"""
CS373: Quiz #16 (5 pts) <Jake>
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following?
    (4 pts)

[2, 3, 4]
[2, 3, 4, 5]
[6, 7, 8]
[6, 7, 8, 9]
"""

class A :
    v = [2, 3, 4]

x = A()
print(x.v)

x.v += [5]
print(x.v)

x.v = [6, 7, 8]
print(x.v)

x.v += [9]
print(x.v)
