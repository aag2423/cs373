#!/usr/bin/env python

# ------------
# Coverage4.py
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

print "Coverage4.py"

test(False, False)
test(False, True)
test(True,  False)
test(True,  True)

print "Done."

"""
% coverage run --branch Coverage4.py
Coverage4.py
b is false and c is false
b is false and c is true
b is true and c is false
b is true and c is true
Done.

% coverage report
Name        Stmts   Miss Branch BrMiss  Cover
---------------------------------------------
Coverage4      15      0      6      0   100%
"""
