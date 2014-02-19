#!/usr/bin/env python3

# -----------
# Closures.py
# -----------

print("Closures.py")

class A :
    def __init__ (self) :
        self.a = []

    def get (self) :
        return self.a

    def add (self, v) :
        self.a.append(v)

x = A()
assert(x.get() == [])
x.add(2)
assert(x.get() == [2])
x.add(3)
assert(x.get() == [2, 3])
x.a[0] = 4
assert(x.get() == [4, 3])
x.a = "gone"
assert(x.get() == "gone")

def A () :
    a = []

    class B :
        def get (self) :
            return a

        def add (self, v) :
            a.append(v)

    return B()

x = A()
assert(x.get() == [])
x.add(2)
assert(x.get() == [2])
x.add(3)
assert(x.get() == [2, 3])
#x.a[0] = 4               # AttributeError: 'A' object has no attribute 'a'
assert(x.get() == [2, 3])
x.a = "gone"              # ?
assert(x.get() == [2, 3])

print("Done.")
