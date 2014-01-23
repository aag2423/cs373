#!/usr/bin/env python

"""
CS373: Quiz #1 (5 pts) <Prateek>
"""

""" ----------------------------------------------------------------------
 1. Given positive integers, b and e, let m = e / 2. If b < m, then
    max_cycle_length(b, e) = max_cycle_length(m, e). True or False?
    [Collatz]
    (1 pt)

True

Consider b = 10, e = 100.
Then m = 100 / 2 = 50.
max_cycle_length(10, 100) = max_cycle_length(50, 100)
All the numbers in the range [10, 49] can be mapped to numbers in the
range [50, 100] by one or more doublings, so none of the numbers in the
range [10, 49] could have a larger cycle length than the numbers in the
range [50, 100].
"""

""" ----------------------------------------------------------------------
 2. What is the output of the following?
    (2 pts)

5 11
"""

def f (n) :
    return n + (n >> 1) + 1

print f(3),
print f(7)

""" ----------------------------------------------------------------------
 3. In the context of Project #1: Collatz, what is f() computing?
    (1 pt)

For odd n it's computing (3n + 1) / 2.
(3n + 1) / 2
3n/2 + 1/2
n + n/2 + 1/2
n + n/2 + 1, because n is odd
n + (n >> 1) + 1
"""
