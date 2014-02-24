#!/usr/bin/env python3

# -------
# Copy.py
# -------

from copy import copy, deepcopy

print("Copy.py")

class A :
    def __init__ (self) :
        self.a = [2, 3, 4]

x = A()
y = A()
assert(x   is not y)
assert(x.a is not y.a)
assert(x.a ==     y.a)

z = copy(x)
assert(x   is not z)
assert(x.a is     z.a)

z = deepcopy(x)
assert(x   is not z)
assert(x.a is not z.a)
assert(x.a ==     z.a)

print("Done.")
