#!/usr/bin/env python3

"""
CS373: Quiz #14 (5 pts) <Jake>
"""

""" ----------------------------------------------------------------------
 1. Fill in the TWO blanks below.
    [The Open-Closed Principle]
    (2 pts)

    Software entities (classes, modules, functions, etc.) should be open
    for <BLANK>, but closed for <BLANK>.

extension
modification
"""

""" ----------------------------------------------------------------------
 2. What is the output of the following?
    (2 pts)

[2, 3]
[2, 3, 4]
"""

def f () :
    a = [2]

    def g (v) :
        a.append(v)
        return a

    return g

x = f()
print(x(3))
print(x(4))
