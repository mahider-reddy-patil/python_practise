class employee:

    _organizationName="XYZ"
    def __init__(self,name,employeeid):
        self.name=name
        self.employeeid=employeeid
    def work(self):
        print("employee working")

    def nameWithWork(self,name,employeeid):
        print("employee name",self.name, " ,id =",self.employeeid)

    def updateOrganizationName(self,changeName):
        self.organizationName=changeName

    def getOrganizationName(self):
        return self.organizationName

    '''
    def __str__(self):
        return f'Emplohyee ({self.name,self.employeeid})'
    '''

    def __repr__(self):
        return f'{self.name,self.employeeid}'


emp1=employee('A',1)
emp2=employee('B',2)
'''
print(emp1.name)
#print(employee.organizationName)
#emp1.nameWithWork('A',1)

emp1.updateOrganizationName('ABC')

print(emp1.getOrganizationName())

print(emp1.organizationName)

'''

print(emp1.__repr__())
