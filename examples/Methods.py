#!/usr/bin/env python3

# ----------
# Methods.py
# ----------

print("Methods.py")

class A :
    __cv = 0

    def __init__ (self) :
        A.__cv    += 1
        self.__iv  = 0
#       cm()           # NameError: global name 'cm' is not defined
        A.cm()
        self.cm()
#       im()           # NameError: global name 'im' is not defined
#       A.im()         # TypeError: unbound method im() must be called with A instance as first argument (got nothing instead)
        self.im()

    @staticmethod
    def cm () :
        A.__cv    += 1
#       self.__iv += 1 # NameError: global name 'self' is not defined
#       self.im()      # NameError: global name 'self' is not defined

    def im (self) :
        A.__cv    += 1
        self.__iv += 1
#       cm()           # NameError: global name 'cm' is not defined
        A.cm()
        self.cm()

A.cm()
#A.im() # TypeError: unbound method im() must be called with A instance as first argument (got nothing instead)

x = A()
x.cm()
x.im()
A.im(x) # methods are really just functions

print("Done.")
