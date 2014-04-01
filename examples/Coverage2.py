#!/usr/bin/env python

# ------------
# Coverage2.py
# ------------

def test (b, c) :
    if b :
        if c :
            print("b is true and c is true")
        else :
            print("b is true and c is false")
    elif c :
        print("b is false and c is true")
    else :
        print("b is false and c is false")

print "Coverage.py"

test(False, False)
test(False, True)

print "Done."

"""
% coverage run --branch Coverage2.py
Coverage.py
b is false and c is false
b is false and c is true
Done.

% coverage report
Name        Stmts   Miss Branch BrMiss  Cover
---------------------------------------------
Coverage2      12      3      6      3    67%
"""
