list =[3,2,1]


person={"name":"AMOL",
        "age":18,
        "gender":"male"}

print(person)

#print(person["gender"])

for key,value in person.items():
        print(person[key])

print("values = ",person.values())
print("keys = ",person.keys())

print("items = ",person.items())

person['division']='A'



person.update({"name":"Ashish","newKey":10})
#person.pop("gender")
person.popitem()
print("items after modification = ",person.items())

print(person.get("name"))

copyOfPerson=person.copy()

print(copyOfPerson)

list=('A','B','C')
values=[10,20]

newDictonaryFromKeys=person.fromkeys(list,values)

print(newDictonaryFromKeys['A'])




