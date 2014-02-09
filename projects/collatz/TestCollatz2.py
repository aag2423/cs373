#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestCollatz.py >& TestCollatz.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py >& TestCollatz.out
"""

# -------
# imports
# -------

import io
import unittest

from Collatz2 import collatz_read_1, collatz_read_2, collatz_read_3, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = io.StringIO("1 10\n")
        a = collatz_read_1(r)
        i, j = list(next(a))
        self.assertTrue(i ==  1)
        self.assertTrue(j == 10)

    def test_read_2 (self) :
        r = io.StringIO("1 10\n")
        a = collatz_read_2(r)
        i, j = list(next(a))
        self.assertTrue(i ==  1)
        self.assertTrue(j == 10)

    def test_read_3 (self) :
        r = io.StringIO("1 10\n")
        a = collatz_read_3(r)
        i, j = list(next(a))
        self.assertTrue(i ==  1)
        self.assertTrue(j == 10)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        a       = collatz_eval([(1, 10)])
        i, j, v = list(next(a))
        self.assertTrue(v == 20)

    def test_eval_2 (self) :
        a       = collatz_eval([(100, 200)])
        i, j, v = list(next(a))
        self.assertTrue(v == 125)

    def test_eval_3 (self) :
        a       = collatz_eval([(201, 210)])
        i, j, v = list(next(a))
        self.assertTrue(v == 89)

    def test_eval_4 (self) :
        a       = collatz_eval([(900, 1000)])
        i, j, v = list(next(a))
        self.assertTrue(v == 174)

    # -----
    # print
    # -----

    def test_print (self) :
        w = io.StringIO()
        collatz_print(w, [(1, 10, 20)])
        self.assertTrue(w.getvalue() == "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")
