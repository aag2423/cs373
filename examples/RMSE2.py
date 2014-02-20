#!/usr/bin/env python3

# --------
# RMSE2.py
# --------

import math
import operator
import sys
import time

print("RMSE2.py")
print(sys.version)
print()

def sqre_diff (x, y) :
    return (x - y) ** 2

def rmse_1 (a, p) :
    s = len(a)
    v = sum(map(sqre_diff, a, p))
    return math.sqrt(v / s)

def mean (a) :
    x = list(a)
    return sum(x) / len(x)

def rmse_2 (a, p) :
    return math.sqrt(mean(map(sqre_diff, a, p)))

def bind1st (tf, x) :
    return lambda y, z : tf(x, y, z)

def compose (f, g) :
    return lambda x, y : f(g(x, y))

rmse_3 = compose(math.sqrt, compose(mean, bind1st(map, sqre_diff)))

def test (f) :
    print(f.__name__)
    assert(str(f((2, 3, 4), (2, 3, 4))) == "0.0")
    assert(str(f((2, 3, 4), (3, 4, 5))) == "1.0")
    assert(str(f((2, 3, 4), (4, 3, 2))) == "1.632993161855452")
    a = 1000000 * [1]
    p = 1000000 * [5]
    b = time.clock()
    assert(str(f(a, p)) == "4.0")
    e = time.clock()
    print("%5.3f" % ((e - b) * 1000), "milliseconds")
    print()

test(rmse_1)
test(rmse_2)
test(rmse_3)

print("Done.")

"""
RMSE.py

2.6.1 (r261:67515, Jun 24 2010, 21:47:49)
[GCC 4.2.1 (Apple Inc. build 5646)]

rmse_1
355.406 milliseconds

rmse_2
358.020 milliseconds

<lambda>
358.054 milliseconds

Done.
"""
