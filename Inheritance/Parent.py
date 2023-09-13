class Parent:

    def car(self):
        print("Nexon")

    def home(self):
        print("parent 2000 sqft")


class grandParent:

    def car_grandParent(self):
        print("Nexon")

    def home(self):
        print("grand parent 2000 sqft")

class child(Parent,grandParent):
    def study(self):
        print("study")

class child2(Parent):
    def study(self):
        print("study")





child=child()
child.home()

child2=child2()
child2.home()

