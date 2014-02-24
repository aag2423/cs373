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
assert(x.__eq__(y))
assert(x.__ne__(y))
assert(not(x == y))
assert(    x != y)

class B :
    def __init__ (self) :
        self.a = [2, 3, 4]

    def __eq__ (self, rhs) :
        if not isinstance(rhs, B) :
            return False
        return self.a == rhs.a

x = B()
y = B()
assert(x   is not y)
assert(x.a is not y.a)
assert(x.a ==     y.a)
assert(     x.__eq__(y))
assert(not (x.__ne__(y)))
assert(     x == y)
assert(not (x != y))

class C :
    def __init__ (self) :
        self.a = [2, 3, 4]

    def __eq__ (self, rhs) :
        if not isinstance(rhs, C) :
            return False
        return self.a == rhs.a

    def __ne__ (self, rhs) :
        return not self.__eq__(rhs)

x = C()
y = C()
assert(x   is not y)
assert(x.a is not y.a)
assert(x.a ==     y.a)
assert(     x.__eq__(y))
assert(not (x.__ne__(y)))
assert(     x == y)
assert(not (x != y))

print("Done.")
