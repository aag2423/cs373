#!/usr/bin/env python

# ------------
# Coverage3.py
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

print "Coverage3.py"

test(False, False)
test(False, True)
test(True,  False)

print "Done."

"""
% coverage run --branch Coverage3.py
Coverage3.py
b is false and c is false
b is false and c is true
b is true and c is false
Done.

% coverage report
Name        Stmts   Miss Branch BrMiss  Cover
---------------------------------------------
Coverage3      13      1      6      1    89%
"""
