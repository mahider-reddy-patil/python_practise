class customerinfo:
    organization='xyz'

    def __init__(self,customerid,customername):
        self.id=customerid
        self.name=customername

    def addcustomer(self,customerid,customername):
        #print("adding customers ")
        print('customer id = ',customerid, "customer name = " ,customername)

    def printvaribale(self):
        print("print values")


'''
objcustomer1=customerinfo() #create object
objcustomer2=customerinfo() #create object

objcustomer1.addcustomer(1,'A')
objcustomer2.addcustomer(2,'B')

objcustomer1.printvaribale()

objcustomer2.printvaribale()

print("accessing the org = ",customerinfo.organization)


'''


obj1=customerinfo(1,'A')
obj2=customerinfo(2,'B')
print(obj1.id)
print(obj1.name)

print(obj2.id)
print(obj2.name)