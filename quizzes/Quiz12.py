#!/usr/bin/env python3

"""
CS373: Quiz #12 (5 pts) <Jake>
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following?
    (2 pts)

0 1 2 3 4 else
0 1 2 3
"""

for v in range(5) :
    print(v, end = " ")
else :
    print("else")

for v in range(5) :
    print(v, end = " ")
    if v == 3 :
        print()
        break
else :
    print("else")

""" ----------------------------------------------------------------------
 2. What is the output of the following?
    (2 pts)

[10]
[]
"""

a = [2, 3, 4]
b = [5, 6, 7]
z = (x + y for x in a if x % 2 for y in b if y % 2)
b[0] = 6
print(list(z))
print(list(z))
