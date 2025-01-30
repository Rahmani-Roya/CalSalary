from dataclasses import dataclass
from typing import List
@dataclass
class Personel:
    name: str
    id: str
    salary: float
    employee : list['Personel']


def cal_salary_set(p: Personel):
    total_salary = p.salary 
    for i in p.employee:
        total_salary += cal_salary_set(i)
    return total_salary

p1 = Personel('Ali','001',1000,[])
p2 = Personel('Aref','002',2000,[])
p3 = Personel('fati','003',1000,[])
p4 = Personel('hasan','004',3000,[p1, p2])
p5 = Personel('moha','005',4000,[p4,p3])
p6 = Personel('Roya','006',7000,[p5])

print(cal_salary_set(p6))