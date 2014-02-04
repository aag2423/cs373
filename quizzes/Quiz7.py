#!/usr/bin/env python3

"""
CS373: Quiz #7 (5 pts) <Prateek>
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following?
    (4 pts)

m1 f1 f2 m2 m4 m5 m6
m1 f1 m3 m5 m6
"""

def f (b) :
    print("f1", end = " ")
    if b :
        raise Exception()
    print("f2", end = " ")

try :
    print("m1", end = " ")
    f(False)
    print("m2", end = " ")
except Exception :
    print("m3", end = " ")
else :
    print("m4", end = " ")
finally :
    print("m5", end = " ")
print("m6")

try :
    print("m1", end = " ")
    f(True)
    print("m2", end = " ")
except Exception :
    print("m3", end = " ")
else :
    print("m4", end = " ")
finally :
    print("m5", end = " ")
print("m6")
