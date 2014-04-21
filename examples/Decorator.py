#!/usr/bin/env python3

# -------------
# Decorator1.py
# -------------

class Window :
    def draw (self) :
        return "Window.draw()"

class DrawableDecorator :
    def __init__ (self, d, s) :
        self.d = d
        self.s = s

    def draw (self) :
        return self.s + " " + self.d.draw()

print("Decorator1.py")

w = Window()
assert w.draw() == "Window.draw()"

w = DrawableDecorator(w, "Decoration1")
assert w.draw() == "Decoration1 Window.draw()"

w = DrawableDecorator(w, "Decoration2")
assert w.draw() == "Decoration2 Decoration1 Window.draw()"

w = DrawableDecorator(w, "Decoration3")
assert w.draw() == "Decoration3 Decoration2 Decoration1 Window.draw()"

print("Done.")
