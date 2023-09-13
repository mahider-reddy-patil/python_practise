class Apple:
    def __init__(self,name,age):
        self.i=name
        self.j=age

    def updateAge(self):
        self.j=18


applevar1=Apple(1000,2000)
applevar2=Apple(8888,7777)
applevar1.updateAge()
print("i name = ",applevar1.i)
print("j age = ",applevar1.j)

print("name value applevar2 = ",applevar2.i)
print("age value applevar2 = ",applevar2.j)
