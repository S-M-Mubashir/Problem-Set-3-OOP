# Question 4
from Question_2 import Publication

class Disk(Publication):
    diskType = " "

    def get_data(self):
        super().get_data()
        types = { "C" : "CD" , "D" : "DVD" }
        print(''' Select one of the following types:
- C for "CD"
- D for "DVD" ''')
        choice = input()
        if choice.lower() == "c":
            self.diskType = types.get("C")
        if choice.lower() == "d":
            self.diskType = types.get("D")

    def put_data(self):
        return f"{super().put_data()} \nDisk Type: {self.diskType}"

D = Disk()
D.get_data()
print(D.put_data())
