#!/usr/bin/env python3

"""
CS373: Quiz #15 (5 pts) <Prateek>
"""

""" ----------------------------------------------------------------------
 1. What kind of table is needed to represent a many-to-many association?
    [UML Design: Many-to-many]
    (1 pts)

join or junction table
"""

""" ----------------------------------------------------------------------
 2. What is the output of the following?
    (3 pts)

4
9
16
"""

import operator

def bind2nd (bf, y) :
    return lambda x : bf(x, y)

def compose (f, g) :
    return lambda x, y : f(g(x, y))

f = bind2nd(operator.pow, 2)
g = compose(f, operator.sub)

print(g(2, 4))
print(g(6, 3))
print(g(5, 9))
