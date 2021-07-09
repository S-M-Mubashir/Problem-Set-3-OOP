# Question 17
class BasicSalary:

    def __init__(self, salary = 10000):
        self.basic = salary
        
    def annualBasicSalary(self):
        return self.basic * 12

class Employee:

    def __init__(self,salary = 1000, bonus = 500):
        self.object_basicSalary = BasicSalary(salary)
        self.annualBonus = bonus

    def annualNetSalary(self):
        return self.object_basicSalary.annualBasicSalary() + self.annualBonus

E = Employee(350000, 1000)
print(E.annualNetSalary())


# Question 18

# Relationship is Composition in Question 17
