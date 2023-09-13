'''
setVariables={1,2,3}
emptySet=set()
print("type of set = ",emptySet)

numberslist=[10,20,30]
numbersTuple=(10,20,30,20,30,50,50,50,50,50,50,50)
listToSet=set(numberslist)
tupleToSet=set(numbersTuple)
print("type of tupleToSet = ",tupleToSet)

tupleToSet.update(0)

print("tupleToSet after adding 60= ",tupleToSet)
'''
list1=[1,2,3]
list2=[2,3]

#print(set1.difference(set2))
#set1.difference_update(set2)
set1=frozenset(list1)
set2=set(list2)


print(set1)


