#!/usr/bin/env python3

# ---------
# Select.py
# ---------

print("Select.py")

def select_1 (r, up) :
    x = []
    for v in r :
        if up(v) :
            x.append(v)
    return x

def select_2 (r, up) :
    return [v for v in r if up(v)]

r = [ \
    {"A" : 1, "B" : 6},
    {"A" : 2, "B" : 7},
    {"A" : 3, "B" : 8}]
assert(len(r) == 3)

s = [ \
    {"A" : 4, "C" : 6},
    {"A" : 1, "C" : 7},
    {"A" : 2, "C" : 8},
    {"A" : 2, "C" : 9}]
assert(len(s) == 4)

def test (f) :
    x = f(r, lambda v : v["B"] > 6)
    assert(len(x) == 2)
    assert(x ==
        [{'A': 2, 'B': 7},
         {'A': 3, 'B': 8}])

test(select_1)
test(select_2)

print("Done.")
