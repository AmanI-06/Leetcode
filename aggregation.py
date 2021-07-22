"""an employee may belong to one or more departments in an organization. 
However, if an employee’s department is deleted, the employee object 
would not be destroyed but would live on. Note that the relationships 
between objects participating in an aggregation cannot be reciprocal—i.e.,
 a department may “own” an employee, 
but the employee does not own the department."""



class A(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def addNums():
        self.b + self.c

class B(object):
    def __init__(self, d, e, A):
        self.d = d
        self.e = e
        self.A = A

    def addAllNums(self):
        x = self.d + self.e + self.A.b + self.A.c
        return x

ting = A("yo", 2, 6)
ling = B(5, 9, ting)

print(ling.addAllNums())