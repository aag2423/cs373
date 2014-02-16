#!/usr/bin/env python3

# ----------------
# FunctionTuple.py
# ----------------

print("FunctionTuple.py")

def f (x, y, *z) :
    assert(type(z) is tuple)
    return [x, y, z]

assert(f(2, 3)       == [2, 3, ()])
assert(f(2, 3, 4)    == [2, 3, (4,)])
assert(f(2, 3, 4, 5) == [2, 3, (4, 5)])

t = (3, 4)
assert(t           == (3, 4))
assert(t           != (4, 3))
assert(f(2, t,  5) == [2, (3, 4), (5,)])
assert(f(2, 5,  t) == [2, 5, ((3, 4),)])
assert(f(2, 5, *t) == [2, 5, (3, 4)])
#f(2, y = 5, *t)                          # TypeError: f() got multiple values for argument 'y'

l = [3, 4]
assert(l           == [3, 4])
assert(l           != [4, 3])
assert(f(2, l,  5) == [2, [3, 4], (5,)])
assert(f(2, 5,  l) == [2, 5, ([3, 4],)])
assert(f(2, 5, *l) == [2, 5, (3, 4)])
#f(2, y = 5, *l)                          # TypeError: f() got multiple values for argument 'y'

s = {3, 4}
assert(s           == {4, 3})
assert(s           == {3, 4})
assert(f(2, s,  5) == [2, {3, 4}, (5,)])
assert(f(2, 5,  s) == [2, 5, ({3, 4},)])
assert(f(2, 5, *s) == [2, 5, (3, 4)])
#f(2, y = 5, *s)                          # TypeError: f() got multiple values for argument 'y'

d = {"b" : 4, "a" : 3}
assert(d                    == {'b' : 4, 'a' : 3})
assert(d                    == {'a' : 3, 'b' : 4})
assert(f(2, d,  5)          == [2, {'a' : 3, 'b' : 4}, (5,)])
assert(f(2, 5,  d)          == [2, 5, ({'a' : 3, 'b' : 4},)])
assert(f(2, 5, *d.keys())   == [2, 5, ('a', 'b')])
assert(f(2, 5, *d.values()) == [2, 5, (3, 4)])
assert(f(2, 5, *d.items())  == [2, 5, (('a', 3), ('b', 4))])
assert(f(2, 5, *d)          == [2, 5, ('a', 'b')])
#f(**d))                                                     # TypeError: f() got an unexpected keyword argument 'a'

d = {"y" : 3}
assert(f(2, **d) == [2, 3, ()])
#f(**d)                         # TypeError: f() takes at least 2 arguments (1 given)

d = {"y" : 3, "z" : 2}
#f(2, **d)              # TypeError: f() got an unexpected keyword argument 'z'
#f(**d)                 # TypeError: f() got an unexpected keyword argument 'z'

d = {"y" : 3, "x" : 2}
#f(2, **d)                   # TypeError: f() got multiple values for keyword argument 'x'
assert(f(**d) == [2, 3, ()])

print("Done.")
