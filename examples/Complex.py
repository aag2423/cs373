#!/usr/bin/env python3

# ----------
# Complex.py
# ----------

print("Complex.py")

class My_Complex :
    def __init__ (self, r = 0, i = 0) :
        self.r = r
        self.i = i

    def __add__ (self, rhs) :
        return My_Complex(self.r + rhs.r, self.i + rhs.i)

    def __eq__ (self, rhs) :
        if not isinstance(rhs, My_Complex) :
            return False
        return (self.r == rhs.r) and (self.i == rhs.i)

    def __str__ (self) :
        return "(" + str(self.r) + ", " + str(self.i) + ")"

    def __sub__ (self, rhs) :
        return My_Complex(self.r - rhs.r, self.i - rhs.i)

    def __isub__ (self, rhs) :
        return self - rhs

    def conjugate (self) :
        self.i = -self.i
        return self

def conjugate (rhs) :
    return My_Complex(rhs.r, rhs.i).conjugate()

x = My_Complex()
y = My_Complex(2)
y = My_Complex(i = 2)
y = My_Complex(r = 3)
z = My_Complex(2, 3)

assert(z.__str__() == "(2, 3)")
assert(str(z)      == "(2, 3)")

t = z.__add__(z)
assert(z == My_Complex(2, 3))
assert(t == My_Complex(4, 6))

t = z + z
assert(z == My_Complex(2, 3))
assert(t == My_Complex(4, 6))

# t.__iadd__(z)                # AttributeError: 'My_Complex' object has no attribute '__iadd__'
# assert(z == My_Complex(2, 3))
# assert(t == My_Complex(6, 9))

t += z
assert(z == My_Complex(2, 3))
assert(t == My_Complex(6, 9))

t = z.__sub__(z)
assert(z == My_Complex(2, 3))
assert(t == My_Complex(0, 0))

t = z - z
assert(z == My_Complex(2, 3))
assert(t == My_Complex(0, 0))

t = t.__isub__(z)
assert(z == My_Complex( 2,  3))
assert(t == My_Complex(-2, -3))

t -= z
assert(z == My_Complex( 2,  3))
assert(t == My_Complex(-4, -6))

t = z.conjugate()
assert(z == My_Complex(2, -3))
assert(t is z)

t = My_Complex.conjugate(z)
assert(z == My_Complex(2, 3))
assert(t is z)

u = conjugate(z)
assert(z == My_Complex(2,  3))
assert(u == My_Complex(2, -3))

print("Done.")
