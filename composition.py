"""Composition is a specialized form of aggregation. In composition,
 if the parent object is destroyed, then the child objects also 
 cease to exist. Composition is actually a strong type of aggregation
and is sometimes referred to as a “death” relationship.
As an example, a house may be composed of one or more rooms. If the house is destroyed, 
then all of the rooms that are part of the house are also destroyed. """


class A(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def addNums():
        self.b + self.c

class B(object):
    def __init__(self, d, e):
        self.d = d
        self.e = e
        self.A = A("yo", 2, 6)

    def addAllNums(self):
        x = self.d + self.e + self.A.b + self.A.c
        return x

ling = B(5, 9)

print(ling.addAllNums())