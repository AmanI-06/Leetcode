"""imagine the relationship between a doctor and a patient.
 A doctor can be associated with multiple patients.
At the same time, one patient can visit multiple doctors for 
treatment or consultation. Each of these objects has its own life cycle and there 
is no “owner” or parent. The objects that are part of 
the association relationship can be created and destroyed independently."""


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

    def addAllNums(self, Ab, Ac):
        x = self.d + self.e + Ab + Ac
        return x

ting = A("yo", 2, 6)
ling = B(5, 9)

print(ling.addAllNums(ting.b, ting.c))