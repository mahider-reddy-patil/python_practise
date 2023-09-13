numbers=[1,2,1,2,3]

numberSet=set(numbers)
print(type(numberSet))
print((numberSet))

fruits={'mango','banana','mango','mango'}

print((fruits))

for items in fruits:
    print('items in set = ',items)

numbersTuple=(10,20,30,40)
setfromTuple=set(numbersTuple)
copyVariable=setfromTuple.copy()
print("setfromTuple = ",setfromTuple)

setfromTuple.add(50)

print("after adding element in setfromTuple = ",setfromTuple)

setfromTuple.pop()

print("after removing element from setfromTuple = ",setfromTuple)

#setfromTuple.discard(20)

print("after discarding element from setfromTuple = ",setfromTuple)

print("direct output = " ,"20" in setfromTuple)

if 20 in setfromTuple:
    print("value present in set")
else:
    print("value NOT present in set")


setfromTuple.remove(20)
setfromTuple.remove(50)

print("after removing element from setfromTuple = ",setfromTuple)

setfromTuple.clear()

print("clear all elements from set = ",setfromTuple)



print("copyVariable = ",copyVariable)

print("intersection = ",copyVariable.intersection(setfromTuple))


print("difference = ",setfromTuple.difference(copyVariable))

print("subset = ",setfromTuple.issubset(copyVariable))
print("superset = ",copyVariable.issuperset(setfromTuple))


newSet={'red','blue','black'}
unionVar = copyVariable.union(numberSet,fruits,newSet)
unionVar1= copyVariable.union(numberSet,fruits,newSet)
print("unionVar = ",unionVar)
print("unionVar1 = ",unionVar1)