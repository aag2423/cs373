#!/usr/bin/env python3

"""
CS373: Quiz #13 (5 pts) <Pradeep>
"""

""" ----------------------------------------------------------------------
 1. What is a primary key?
    [Basic UML & SQL: Rows & Tables]
    (1 pt)

a minimal unique identifier for each row
"""

""" ----------------------------------------------------------------------
 2. What is the multiplicity of an association?
    [Basic UML & SQL: Associations]
    (1 pt)

how many instances of a class are connected to an instance of another
class
"""

""" ----------------------------------------------------------------------
 3. What is the output of the following?
    (2 pts)

[2, 3, 4, 5, 7]
"""

def f (x, y, z, a = 5, b = 6) :
    return [x, y, z, a, b]

t = (3,)
d = {"b" : 7}

print(f(2, z = 4, *t, **d))
