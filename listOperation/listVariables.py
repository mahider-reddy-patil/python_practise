numberlistVaribles=[1,2,3,4,5]
stringlistVaribles=['Red','Blue','yellow']
numberlistVaribles.sort(reverse=False)
print("reverse the numbers= ",numberlistVaribles)
albhabetList=['A','B','C','D','E','F','G','H','I','J']

print(type(albhabetList))

print(albhabetList[0])

#first three elemenst to print
print(albhabetList[:3])

print(albhabetList[2:])

for alphabate in albhabetList:
    print(alphabate)
    if alphabate=='D':
        break

print(" 0th element = ",albhabetList[0])

print(" 0th element = ",albhabetList[0])

print(" 0th element = ",albhabetList.index("J"))

albhabetList.append("K")
print(albhabetList)

albhabetList.insert(50,"City")
print(albhabetList)


print(" 0th element = ",albhabetList.index("City"))

del albhabetList[0]

print(albhabetList)

albhabetList.pop(3)

print(" pop " , albhabetList)

concatenatedList=numberlistVaribles+stringlistVaribles
print("concatenate two list = ",concatenatedList)

print("concatenate two list type = ",type(concatenatedList))

concatenatedListWithAppend=numberlistVaribles.append(stringlistVaribles)

print("concatenate two list with Append= ",concatenatedListWithAppend)
