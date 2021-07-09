# Question 24
class Time:

    def __init__(self, hrs = 0 , mins = 0 , secs = 0):
        self.hours = hrs
        self.minutes = mins
        self.seconds = secs

    def printTime(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def __add__(self, t):
        if type(t) == Time:
            self.seconds += t.seconds
            if self.seconds >= 60:
                self.seconds -= 60
                self.minutes += 1
            self.minutes += t.minutes
            if self.minutes >= 60:
                self.minutes -= 60
                self.hours += 1
            self.hours += t.hours
        else:
            print("Invalid Data Type")

    def __sub__(self,t):
        if type(t) == Time:
            self.seconds -= t.seconds
            self.seconds = abs(self.seconds)
            if self.seconds >= 60:
                self.minutes -= 1
            self.minutes -= t.minutes
            self.minutes = abs(self.minutes)
            if self.minutes >= 60:
                self.hours -= 1
            self.hours -= t.hours
            self.hours = abs(self.hours)
        else:
            print("Invalid Data Type")

    def __mul__(self,multiplier):
        if self.hours != 0:
            self.hours *= multiplier
        elif self.minutes != 0:
            self.minutes *= multiplier
        elif self.seconds != 0:
            self.seconds *= multiplier
            
T1 = Time(4,56,20)
T2 = Time(7,20,45)
print(f"Object Number 1: {T1.printTime()}")
print(f"Object Number 2: {T2.printTime()}")

T1 - T2
print(f"New Time: {T1.printTime()}")

T3 = Time(5,20,55)
T3 * 2.0
print(f"{T3.printTime()}")
