#!/usr/bin/env python3

# -------
# RMSE.py
# -------

import functools
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

def rmse_for_zip_range (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    s = len(a)
    v = 0.0
    for i in range(s) :
        v += (a[i] - p[i]) ** 2
        i += 1
    return math.sqrt(v / s)

def rmse_for_zip (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    s = len(a)
    z = zip(a, p)
    v = 0.0
    for x, y in z :
        v += (x - y) ** 2
    return math.sqrt(v / s)

def rmse_reduce (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    s = len(a)
    z = zip(a, p)
    v = functools.reduce(lambda v, a : v + (a[0] - a[1]) ** 2, z, 0.0)
    return math.sqrt(v / s)

def rmse_sum_map (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    s = len(a)
    v = sum(map(lambda x, y : (x - y) ** 2, a, p), 0.0)
    return math.sqrt(v / s)

def rmse_sum_list_zip (a, p) :
    """
    O(n) in space
    O(n) in time
    """
    s = len(a)
    z = zip(a, p)
    v = sum([(x - y) ** 2 for x, y in z], 0.0)
    return math.sqrt(v / s)

def rmse_sum_gen_zip (a, p) :
    """
    O(1) in space
    O(n) in time
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
    a = 100000 * [1]
    p = 100000 * [5]
    b = time.clock()
    assert(str(f(a, p)) == "4.0")
    e = time.clock()
    print("%5.3f" % ((e - b) * 1000), "milliseconds")
    print()

print("RMSE.py")
print(sys.version)
print()

test(rmse_while)
test(rmse_for_zip_range)
test(rmse_for_zip)
test(rmse_reduce)
test(rmse_sum_map)
test(rmse_sum_list_zip)
test(rmse_sum_gen_zip)

print("Done.")

"""
RMSE.py
3.3.3 (default, Jan 19 2014, 10:13:09)
[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.2.79)]

rmse_while
41.915 milliseconds

rmse_for_zip_range
41.233 milliseconds

rmse_for_zip
34.312 milliseconds

rmse_reduce
45.215 milliseconds

rmse_sum_map
35.277 milliseconds

rmse_sum_list_zip
35.209 milliseconds

rmse_sum_gen_zip
32.994 milliseconds

Done.
"""
