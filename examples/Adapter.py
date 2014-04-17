#!/usr/bin/env python

# ----------
# Adapter.py
# ----------

# http://en.wikipedia.org/wiki/Adapter_pattern

print "Adapter.py"

class Stack :
    def __init__ (self) :
        self.a = []

    def empty (self) :
        return not self.a

    def pop (self) :
        self.a.pop()

    def push (self, v) :
        self.a.append(v)

    def top (self) :
        return self.a[-1]

s = Stack()
s.push(2)
s.push(3)
s.push(4)
assert s.top() == 4
s.pop()
assert s.top() == 3

print "Done."
