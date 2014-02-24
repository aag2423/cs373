#!/usr/bin/env python3

# ---------
# Equals.py
# ---------

print("Equals.py")

class A :
    def __init__ (self) :
        self.a = [2, 3, 4]

x = A()
y = A()
assert(x   is not y)
assert(x.a is not y.a)
assert(x.a ==     y.a)
assert(x   !=     y)

class B :
    def __init__ (self) :
        self.a = [2, 3, 4]

    def __eq__(self, rhs) :
        if not isinstance(rhs, B) :
            return False
        return self.a == rhs.a

x = B()
y = B()
assert(x   is not y)
assert(x.a is not y.a)
assert(x.a ==     y.a)
assert(x   ==     y)

print("Done.")
