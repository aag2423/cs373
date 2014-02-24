#!/usr/bin/env python3

# -----------------
# ClassVariables.py
# -----------------

print("ClassVariables.py")

class A :
#   v                   # NameError: name 'v' is not defined
    v0     = 0
#   v1     =   A.v0 + 1 # NameError: name 'A' is not defined
    v1     =     v0 + 1
    v1     =     v0 + 1 # same as above
    __v2   =     v1 + 1 # __v2 and _A__v2 become synonymous
    __v2   =     v1 + 1 # same as above
    _A__v3 =   __v2 + 1 # __v3 and _A__v3 become synonymous
    _A__v3 = _A__v2 + 1 # same as above

assert(hasattr(A, "__dict__"))

assert(hasattr(A, "v0"))
assert(A.v0             == 0)
assert(A.__dict__["v0"] == 0)

assert(hasattr(A, "v1"))
assert(A.v1             == 1)
assert(A.__dict__["v1"] == 1)

assert(not hasattr(A, "__v2"))   # __v2 is private
#assert(A.__v2             == 2) # AttributeError: type object 'A' has no attribute '__v2'
#assert(A.__dict__["__v2"] == 2) # KeyError: '__v2'

assert(hasattr(A, "_A__v2"))      # not really!
assert(A._A__v2             == 2)
assert(A.__dict__["_A__v2"] == 2)

assert(not hasattr(A, "__v3"))   # __v3 is private
#assert(A.__v3             == 3) # AttributeError: type object 'A' has no attribute '__v3'
#assert(A.__dict__["__v3"] == 3) # KeyError: '__v3'

assert(hasattr(A, "_A__v3"))      # not really!
assert(A._A__v3             == 3)
assert(A.__dict__["_A__v3"] == 3)

assert(not hasattr(A, "v4"))
#assert(A.v4             == 4) # AttributeError: type object 'A' has no attribute 'v4'
#assert(A.__dict__["v4"] == 4) # KeyError: 'v4'

A.v4 = [2, 3, 4]
assert(hasattr(A, "v4"))
assert(A.v4             == [2, 3, 4])
assert(A.__dict__["v4"] == [2, 3, 4])

assert(not hasattr(A, "__v5"))
#assert(A.__v5             == 5) # AttributeError: type object 'A' has no attribute 'v4'
#assert(A.__dict__["__v5"] == 5) # KeyError: 'v4'

A.__v5 = [2, 3, 4]
assert(hasattr(A, "__v5"))
assert(A.__v5             == [2, 3, 4])
assert(A.__dict__["__v5"] == [2, 3, 4])

del A.v0
assert(not hasattr(A, "v0"))
#assert(A.v0             == 0) # AttributeError: type object 'A' has no attribute 'v0'
#assert(A.__dict__["v0"] == 0) # KeyError: 'v0'

x = A()
y = A()
assert(A.v4 is x.v4 is y.v4)

print("Done.")
