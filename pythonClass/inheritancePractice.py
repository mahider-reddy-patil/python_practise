class A:
    def function1(self):
        print("function1 from A")

    def function2(self):
        print("function2")

class B():
    def function1(self):
        print("function1 from B")

    def function4(self):
        print("function4")


class C(A,B):
    def function5(self):
        print("function5")

    def function6(self):
        print("function6")

varC=C()
varC.function1()