# Question 15
class Int:
    def __init__(self, v = 0):
        self.variable = v
        
    def change(self, v):
        if type(v) == int:
            self.variable = v
        else:
            print("Wrong data type")
            self.variable = 0
            
    def display(self):
        return self.variable

    def __add__(self, var_1):
        if type(var_1) == Int:
            return self.variable + var_1.variable

a = Int()          # Uninitialized 
b = Int(4)        # Initialized
c = Int(5)        # Initialized

result = b + c           # Adding both initialized objects

a.change(result)        # Changing the uninitialized one with the result
print(a.display())
