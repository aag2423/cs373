#!/usr/bin/env python3

# ------------------
# GlobalVariables.py
# ------------------

print("GlobalVariables.py")

v1 = 1
v2 = 2
v4 = 4
v5 = 5
v6 = 6

def f () :
    assert(v1 == 1) # global

    v2 = 10 # local

    v3 = 11 # local

    try :
        assert(v4 == 4) # local
        assert(False)
    except UnboundLocalError as e :
        assert(len(e.args) == 1)
        assert(e.args      == ("local variable 'v4' referenced before assignment",))
    v4 = 12             # local

    try :
        v5 += 13        # local
        assert(False)
    except UnboundLocalError as e :
        assert(len(e.args) == 1)
        assert(e.args      == ("local variable 'v5' referenced before assignment",))

    global v6           # global
    v6 = 14

v3 = 3

f()

assert(v1 ==  1)
assert(v2 ==  2)
assert(v3 ==  3)
assert(v4 ==  4)
assert(v5 ==  5)
assert(v6 == 14)

print("Done.")
