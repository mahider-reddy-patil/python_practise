x = {'apple','banana','cherry'}
y = {'google','microsoft','apple'}
print("before union x= ",x)
x.update(y)

z=x.union(y)
#{'google', 'banana', 'apple', 'microsoft', 'cherry'}
 #{'apple', 'google', 'banana', 'cherry', 'microsoft'}
print("after union x= ",x)
print("after union y= ",y)
print("set z= ",z)

varString="Amol"
var=isinstance(varString,str)
print(var)


if isinstance(z,set):
    print("set present")
else:
    print("not set")

if type(varString) == str:
    print("str present")
else:
    print("not str")

