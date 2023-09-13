#studentdetailsinit.py
class Student:
    """A simple example class"""
    def __init__(self, sclass, sroll, sname):
        self.c = sclass
        self.r = sroll
        self.n = sname
    def messg(self):
            return 'New Session will start soon.'


x = Student('9th',10,'Amol')

print(x.c)
print(x.r)
print(x.n)