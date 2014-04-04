#!/usr/bin/env python3

"""
CS373: Quiz #29 (5 pts) <Prateek>
"""

""" ----------------------------------------------------------------------
 1. Find the bug in the tests.
    Find the bug in the code.
    (4 pts)

2 is prime
remove check for even
change 3 to 2
add 1 to range
"""

from math import sqrt

def is_prime (n) :
    assert(n > 0)
    if (n < 2) or ((n % 2) == 0) :
        return False
    for i in range(3, int(sqrt(n))) :
        if (n % i) == 0:
            return False
    return True

print("Quiz29.py")

assert(not is_prime( 1));
assert(not is_prime( 2));
assert(    is_prime( 3));
assert(not is_prime( 4));
assert(    is_prime( 5));
assert(not is_prime( 6));
assert(    is_prime( 7));
assert(not is_prime( 8));
assert(    is_prime(17));

print("Done.")

"""
% coverage run --branch Quiz29.py
Quiz29.py
Done.

% coverage report
Name     Stmts   Miss Branch BrMiss  Cover
------------------------------------------
Quiz29      21      1      6      1    93%
"""
