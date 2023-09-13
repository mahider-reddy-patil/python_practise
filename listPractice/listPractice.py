numbers=[10,20,30,40,50,17,45]
#       [45, 17, 50, 40, 30, 20, 10]
varString="Python"
cities=["mumbai","chennai"]
#numbers=[10,20,30]
'''
append
insert
delete
clear
copy 
slicing
unpacking


print(type(numbers))
numbers[3]=99
print(numbers)

numbers.append(60)

print(numbers)

numbers.insert(3,101)


del numbers[2]
print(numbers)
numbers.pop(3)
#numbers.clear()
print(numbers)

newnumbersList=numbers[2:5]
print("newnumbersList = ",newnumbersList)
'''
print("newnumbersList starts with 2 = ",numbers[2:])
print("newnumbersList starts with first index = ",numbers[:4])

#del numbers[1:3]
#numbers.clear()
print("newnumbersList with all element = ",numbers)

newCopyList=numbers

print("newCopyList with all element = ",newCopyList)


var1,var2,*others=numbers

print("var1 = ",type(var1))
print("var2 = ",type(var2))
print("others = ",others)

print("count the elements of 50 = ",numbers.count(10))
'''


numbers.sort(reverse=False)
print("sorted list by using sort function = ",numbers)

sorted(numbers,reverse=True)
print("sorted list = ",sorted(numbers,reverse=True))

print("numbers.index(45) = ",numbers.index(45))
'''
print("lenght of list = ",len(numbers))

#numbers.extend(cities)

print("after reverse first element = ",numbers[1])



