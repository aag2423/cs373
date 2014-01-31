#!/usr/bin/env python3

# -------
# RMSE.py
# -------

import math
import sys
import time

def rmse_while (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    s = len(a)
    i = 0
    v = 0.0
    while i != s :
        v += (a[i] - p[i]) ** 2
        i += 1
    return math.sqrt(v / s)

def rmse_for (a, p) :
    """
    O(1n) in space
    O(2n) in time
    """
    s = len(a)
    z = zip(a, p)
    v = 0.0
    for x, y in z :
        v += (x - y) ** 2
    return math.sqrt(v / s)

def rmse_map (a, p) :
    """
    O(1n) in space
    O(2n) in time
    """
    s = len(a)
    v = sum(map(lambda x, y : (x - y) ** 2, a, p), 0.0)
    return math.sqrt(v / s)

def rmse_list_comp (a, p) :
    """
    O(1n) in space
    O(2n) in time
    """
    s = len(a)
    z = zip(a, p)
    v = sum([(x - y) ** 2 for x, y in z], 0.0)
    return math.sqrt(v / s)

def rmse_gen (a, p) :
    """
    O(1n) in space
    O(1n) in time
    """
    s = len(a)
    z = zip(a, p)
    v = sum(((x - y) ** 2 for x, y in z), 0.0)
    return math.sqrt(v / s)

def test (f) :
    print(f.__name__)
    assert(str(f((2, 3, 4), (2, 3, 4))) == "0.0")
    assert(str(f((2, 3, 4), (3, 4, 5))) == "1.0")
    assert(str(f((2, 3, 4), (4, 3, 2))) == "1.632993161855452")
    a = 1000 * [1]
    p = 1000 * [5]
    b = time.clock()
    assert(f(a, p) == 4)
    e = time.clock()
    print("%5.3f" % ((e - b) * 1000), "milliseconds")
    print()

print("RMSE.py")
print(sys.version)
print()

test(rmse_while)
test(rmse_for)
test(rmse_map)
test(rmse_list_comp)
test(rmse_gen)

print("Done.")

"""
RMSE.py
2.7.2 (default, Oct 11 2012, 20:14:37)
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)]

rmse_while
0.452 milliseconds

rmse_for
0.356 milliseconds

rmse_map
0.425 milliseconds

rmse_list_comp
0.403 milliseconds

rmse_gen
0.339 milliseconds

Done.
"""
