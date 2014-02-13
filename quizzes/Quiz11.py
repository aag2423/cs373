#!/usr/bin/env python3

"""
CS373: Quiz #11 (5 pts) <Prateek>
"""

""" ----------------------------------------------------------------------
 1. In the paper, "A Bug and a Crash" about the Ariane 5, what was the
    software bug?
    (1 pt)

the conversion of a 64-bit number to a 16-bit number
"""

""" ----------------------------------------------------------------------
 2. In the paper, "Mariner 1", what was the software bug?
    (1 pt)

the ommission of a hyphen
"""

""" ----------------------------------------------------------------------
 3. Define the function map().
    (2 pts)
"""

def sqre (x) :
    return x * x

def cube (x) :
    return x * x * x

def map (f, a) :
    return (f(v) for v in a)

assert(list(map(sqre, []))     == [])
assert(list(map(sqre, [2]))    == [4])
assert(list(map(sqre, [2, 3])) == [4, 9])

assert(list(map(cube, []))     == [])
assert(list(map(cube, [2]))    == [8])
assert(list(map(cube, [2, 3])) == [8, 27])
