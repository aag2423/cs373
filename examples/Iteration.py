#!/usr/bin/env python3

# ------------
# Iteration.py
# ------------

import itertools
import operator
import types

print("Iteration.py")

a = [2, 3, 4]
s = 0
for v in a :
    s += v
assert(s == 9)

a = [2, 3, 4]
for v in a :
    v += 1             # ?
assert(a == [2, 3, 4])

a = ["abc", "def", "ghi"]
for v in a :
    v += "x"                       # ?
assert(a == ["abc", "def", "ghi"])

a = [[2], [3], [4]]
for v in a :
    v += (5,)                         # ?
assert(a == [[2, 5], [3, 5], [4, 5]])

a = [(2,), (3,), (4,)]
for v in a :
    v += (5,)                   # ?
assert(a == [(2,), (3,), (4,)])

a = [(2, "abc"), (3, "def"), (4, "ghi")]
s = 0
for u, v in a :
    s += u
assert(s == 9)

d = {2 : "abc", 3 : "def", 4 : "ghi"}
s = 0
for k in d :
    s += k
assert(s == 9)

d = {2 : "abc", 3 : "def", 4 : "ghi"}
s = 0
for k, v in d.items() :
    s += k
assert(s == 9)

x = range(10)
assert(type(x) is range)
assert(list(x) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

x = range(2, 10)
assert(list(x) == [2, 3, 4, 5, 6, 7, 8, 9])

x = range(2, 10, 2)
assert(list(x) == [2, 4, 6, 8])

x = range(10, 2, -2)
assert(list(x) == [10, 8, 6, 4])

x = range(10)
assert(x[0] == 0)
assert(x[9] == 9)
try :
    assert(x[10] == 10) # error: out of range
    assert(False)
except IndexError :
    pass
#x[0] = 2               # TypeError: 'xrange' object does not support item assignment
s = 0
for v in x :
    s += v
assert(s == 45)

x = range(15)
s = 0
for v in x :
    if v == 10 :
        break
    s += v
else :            # else clause in a for loop
    assert(False) # executes when the loop terminates normally
assert(s == 45)

x = itertools.count(0)             # 0, 1, 2, ...
assert(type(x) is itertools.count)
#assert(x[0] == 0)                 # TypeError: 'itertools.count' object is not indexable
s = 0
for v in x :
    if v == 10 :
        break
    s += v
assert(s == 45)

x = itertools.count(3, 2) # 3, 5, 7, 9, ...
s = 0
for v in x :
    if v > 10 :
        break
    s += v
assert(s == 24)

x = [2, 3, 4, 5, 6]
y = []
for v in x :
    y += [v * 5]
assert(x == [ 2,  3,  4,  5,  6])
assert(y == [10, 15, 20, 25, 30])

x = [2, 3, 4, 5, 6]
y = [v * 5 for v in x]                  # list comprehension
assert(type(y) is list)
assert(x       == [2,   3,  4,  5,  6])
assert(y       == [10, 15, 20, 25, 30])

x = [2, 3, 4, 5, 6]
y = map(lambda v : v * 5, x)            # map
assert(type(y) is map)
assert(x       == [2,   3,  4,  5,  6])
assert(list(y) == [10, 15, 20, 25, 30])

x = [2, 3, 4, 5, 6]
y = (v * 5 for v in x)                  # generator
assert(type(y) is types.GeneratorType)
assert(x       == [2,   3,  4,  5,  6])
assert(list(y) == [10, 15, 20, 25, 30])
assert(list(y) == [])

x = [2, 3, 4, 5, 6]
y = []
for v in x :
    if v % 2 :
        y += [v * 5]
assert(x == [2, 3, 4, 5, 6])
assert(y == [15, 25])

x = [2, 3, 4, 5, 6]
y = [v * 5 for v in x if v % 2]
assert(type(y) is list)
assert(x       == [2, 3, 4, 5, 6])
assert(y       == [15, 25])

x = [2, 3, 4, 5, 6]
y = filter(lambda v : v % 2, x)
assert(type(y) is filter)
z = map(lambda v : v * 5, y)
assert(type(z) is map)
assert(x       == [2, 3, 4, 5, 6])
assert(list(z) == [15, 25])

x = [2, 3, 4, 5, 6]
y = (v * 5 for v in x if v % 2)
assert(type(y) is types.GeneratorType)
assert(x       == [2, 3, 4, 5, 6])
assert(list(y) == [15, 25])
assert(list(y) == [])

x = [2, 3, 4]
y = [4, 5]
z = []
for v in x :
    for w in y :
        z += [v + w]
assert(x == [2, 3, 4])
assert(y == [4, 5])
assert(z == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5])
assert(z == [6, 7, 7, 8, 8, 9])

x = [2, 3, 4]
y = [4, 5]
z = [v + w for v in x for w in y]
assert(type(z) is list)
assert(x       == [2, 3, 4])
assert(y       == [4, 5])
assert(z       == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5])
assert(z       == [6, 7, 7, 8, 8, 9])

x = [2, 3, 4]
y = [4, 5]
z = (v + w for v in x for w in y)
assert(type(z) is types.GeneratorType)
assert(x       == [2, 3, 4])
assert(y       == [4, 5])
assert(list(z) == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5])
assert(list(z) != [6, 7, 7, 8, 8, 9])
assert(list(z) == [])

x = {2 : "abc", 3 : "def", 4 : "ghi"}
y = {}
for k, v in x.items() :
    y[k] = v + "xyz"
assert(x == {2 : "abc", 3 : "def", 4 : "ghi"})
assert(y == {2 : "abcxyz", 3 : "defxyz", 4 : "ghixyz"})

x = {2 : "abc", 3 : "def", 4 : "ghi"}
y = {k : v + "xyz" for k, v in x.items()}
assert(x == {2 : "abc", 3 : "def", 4 : "ghi"})
assert(y == {2 : "abcxyz", 3 : "defxyz", 4 : "ghixyz"})

assert(all([True, 2, 3.45, "abc", [2, 3, 4], (2, 3, 4), {2, 3, 4}]))
assert(not all([False]))
assert(not all([0]))
assert(not all([0.0]))
assert(not all([""]))
assert(not all([[]]))
assert(not all([()]))
assert(not all([{}]))

assert(not any([False, 0, 0.0, "", [], (), {}]))
assert(any([True]))
assert(any([2]))
assert(any([3.45]))
assert(any(["abc"]))
assert(any([[2, 3, 4]]))
assert(any([(2, 3, 4)]))
assert(any([{2, 3, 4}]))

print("Done.")
