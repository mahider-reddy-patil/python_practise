variableTuple=(1, 2, 3, 4, 5, 6, 7, 8, 9)
numbers=[10,20,30,40,50,17,45]
print(type(variableTuple))

#variableTuple[0]=10

print(variableTuple)
i=20
if i in numbers:
    print(f'variable present in list {i}')

for index,value in enumerate(variableTuple):
    print("index = ",index,", value =  ",value)


newTuple=tuple(numbers)
newTupleWithVariable=4,
print(type(newTupleWithVariable))

for i in newTupleWithVariable:
    print("elements of newTupleWithVariable = ",i)

evenCount=0
oddCount=0
for value in variableTuple:
    if value%2==0:
        evenCount=evenCount+1
    else:
        oddCount=oddCount+1

print("evenCount = ",evenCount)
print("oddCount = ",oddCount)

print("------------------------------------")


outputList=[]
for i in range(1500,2701):
    if(i%7==0 and i%5==0):
        outputList.append(i)

print("outputList = ",outputList)

print("------------------------------------")



for i in range(0,7):
    if(i == 3 or i==6):
        continue
    print("value of i = ",i)


