import genericFunctiosPython

from genericFunctiosPython import calculategst
from sys import get_int_max_str_digits
class taxex:
    def calculategst(self,total,taxPercentage):
        return (total*taxPercentage)/100


#objEmp1=taxex()
#totalTax=objEmp1.calculategst(10000,18)

totalTax=calculategst(10000,18)





