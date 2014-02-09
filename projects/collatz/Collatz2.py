#!/usr/bin/env python3

# ----------------------------
# projects/collatz/Collatz2.py
# Copyright (C) 2014
# Glenn P. Downing
# ----------------------------

# ------------
# collatz_read
# ------------

class Itr :
    def __init__ (self, r) :
        self.r = r

    def __iter__ (self) :
        return self

    def __next__ (self) :
        s = self.r.readline()
        if s == "" :
            raise StopIteration()
        return map(int, s.split())

def collatz_read_1 (r) :
    """
    reads a sequence of two ints
    r is a reader
    return an iterator of an iterable of two ints
    """
    return Itr(r)

def collatz_read_2 (r) :
    """
    reads a sequence of two ints
    r is a reader
    return a generator of an iterable of two ints
    """
    for s in r :
        yield map(int, s.split())

def collatz_read_3 (r) :
    """
    reads a sequence of two ints
    r is a reader
    return a generator of an iterable of two ints
    """
    return (map(int, s.split()) for s in r)

# ------------
# collatz_eval
# ------------

def collatz_eval (a) :
    """
    a is an iterable of iterables of two ints, i and j
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return a generator of tuples of i, j, and the max cycle length in the range [i, j]
    """
    return ((i, j, 1) for i, j in a)

# -------------
# collatz_print
# -------------

def collatz_print (w, a) :
    """
    prints the values of i, j, and v
    w is a writer
    a is an iterable of iterables of three ints, i, j, and v
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    for i, j, v in a :
        w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    """
    for m in collatz_read_3(r) :
        i, j = list(m)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
    """
    collatz_print(w, collatz_eval(collatz_read_3(r)))
