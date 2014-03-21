#!/usr/bin/env python3

# ----------
# Project.py
# ----------

print("Project.py")

def project_1 (r, a) :
    x = []
    for v in r :
        y = {}
        for w in a :
            if w in v :
                y[w] = v[w]
        x.append(y)
    return x

def project_2 (r, a) :
    return [{w : v[w] for w in a if w in v} for v in r]

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
    x = f(r, ["B"])
    assert(len(x) == 3)
    assert(x ==
        [{'B': 6},
         {'B': 7},
         {'B': 8}])

test(project_1)
test(project_2)

print("Done.")
