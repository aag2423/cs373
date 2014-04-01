#!/usr/bin/env python

# ------------
# Coverage1.py
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

print "Coverage1.py"

test(False, False)

print "Done."

"""
% coverage run --branch Coverage1.py
Coverage1.py
b is false and c is false
Done.

% coverage report
Name        Stmts   Miss Branch BrMiss  Cover
---------------------------------------------
Coverage1      11      4      6      4    53%
"""
