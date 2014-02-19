#!/usr/bin/env python3

# ----------
# Binders.py
# ----------

import functools
import operator

print("Binders.py")

def bind1st (bf, x) :
    return lambda y : bf(x, y)

def bind2nd (bf, y) :
    return lambda x : bf(x, y)

def flip (bf) :
    return lambda x, y : bf(y, x)

def sqre_1 (n) :
    return n ** 2;

def cube_1 (n) :
    return n ** 3;

sqre_2 = bind2nd(operator.pow, 2)
cube_2 = bind2nd(operator.pow, 3)

sqre_3 = bind1st(flip(operator.pow), 2)
cube_3 = bind1st(flip(operator.pow), 3)

sqre_4 = functools.partial(flip(operator.pow), 2)
cube_4 = functools.partial(flip(operator.pow), 3)

def test (f, g) :
    assert f(2) == 4
    assert g(2) == 8

test(sqre_1, cube_1)
test(sqre_2, cube_2)
test(sqre_3, cube_3)
test(sqre_4, cube_4)

print("Done.")
