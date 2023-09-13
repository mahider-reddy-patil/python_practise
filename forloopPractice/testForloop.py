def testrecurrsiveFunction(num1):
    print('number = ',num1)
    next=num1-1
    if(next>0):
        testrecurrsiveFunction(next)

testrecurrsiveFunction(5)


