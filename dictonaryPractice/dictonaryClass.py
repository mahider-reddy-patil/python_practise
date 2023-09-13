dictVar={"name":"Amol","age":33}

print("dictonary value = ",dictVar.get("age"))

print("items before = ",dictVar.items())

#dictVar.pop("age")
#dictVar.clear()
#print("items after = ",dictVar.values())
#print("items after = ",dictVar.keys())
#print("items after = ",dictVar.items())
print("-------ITERATE KEYS--------------")
for i in dictVar.keys():
    print("key = ",i, " ,value = ",dictVar[i])

print("-------ITERATE VALUES--------------")

for i in dictVar.values():
    print("value = ",i)

'''
print("---------ITERATE ITEMS------------------------")

for key, value in dictVar.items():
    print("key items = ",key," ,value items = ",value)

print("----------------------------------")

print("---------POP ITEMS------------------------")

#dictVar.pop("age")

print("items after = ",dictVar)
print("---------UPDATE ------------------------")
dictVar.update({"name":"Ashish","division":"A"})
dictVar.popitem()

key=["A","B","C"]
value=[1,2,3]
newdictonary={}
newdictonary=dict.fromkeys(key,value)

print("newdictonary = ",newdictonary)
'''