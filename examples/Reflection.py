#!/usr/bin/env python3

# -------------
# Reflection.py
# -------------

print("Reflection.py")

class A () :
    def f (self) :
        return "A.f()"

class B () :
    def __init__ (self, v) :
        self.v = v

def test (a) :
    assert(a().f() == "A.f()")

test(A)
test(type(A()))
test(A().__class__)
test(globals()["A"])

try :
    globals()["B"]()
    assert(False)
except TypeError as e :
    assert(type(e)      is     TypeError)
    assert(type(e.args) is     tuple)
    assert(len(e.args)  is     1)
    assert(e.args       is not ("__init__() missing 1 required positional argument: 'v'",))
    assert(e.args       ==     ("__init__() missing 1 required positional argument: 'v'",))

try :
    globals()["C"]
    assert(False)
except KeyError as e :
    assert(type(e)      is     KeyError)
    assert(type(e.args) is     tuple)
    assert(len(e.args)  is     1)
    assert(e.args       is not ('C',))
    assert(e.args       ==     ('C',))

print("Done.")
