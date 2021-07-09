# Question 25

# Note:
# all the dunder methods ( +, - , * , / ) returns a new Fraction object
# no changes are made in any of the 2 Fraction objects used for the operations
class Fraction:

    @staticmethod
    def Factor(n):
        factor_list = [ ]
        for i in range(1,n + 1):
            if n % i == 0:
                factor_list.append(i)
        return factor_list

    @staticmethod
    def HCF(n1, n2):
        all_factors = n1 + n2
        common_factors = [ ]
        for n in all_factors:
            if (n in n1) and (n in n2):
                common_factors.append(n)
        return max(common_factors)
        
    def __init__(self, num = 0, den = 1):
        self.numerator = num
        if den != 0:
            self.denominator = den
        else:
            self.denominator  = 1

    def set_numerator(self):
        self.numerator = int(input("Enter numerator value: "))
    def get_numerator(self):
        return self.numerator

    def set_denominator(self):
        den = int(input("Enter denominator value: "))
        if den != 0:
            self.denominator = den
        else:
            self.denominator  = 1    
    def get_denominator(self):
        return self.denominator

    def simplify(self):
        num_factors = Fraction.Factor(self.numerator)
        den_factors = Fraction.Factor(self.denominator)
        Hcf = Fraction.HCF(num_factors, den_factors)
        self.numerator = int(self.numerator / Hcf)
        self.denominator = int(self.denominator / Hcf)

    def __add__(self, f):
        if type(f) == Fraction:
            a = self.numerator * f.denominator
            b = f.numerator * self.denominator
            num = a + b
            den = self.denominator * f.denominator
            F = Fraction(num, den)
            F.simplify()
            return F

    def __sub__(self, f):
        if type(f) == Fraction:
            a = self.numerator * f.denominator
            b = f.numerator * self.denominator
            den = self.denominator * f.denominator
            num = a - b
            if num == 0:
                return 0
            else:
                F = Fraction(num, den)
                F.simplify()
                return F
            
    def __mul__(self, f):
        if type(f) == Fraction:
            num = self.numerator * f.numerator
            den = self.denominator * f.denominator
            F = Fraction(num, den)
            F.simplify()
            return F

    def __truediv__(self, f):
        if type(f) == Fraction:
            num = self.numerator * f.denominator
            den = self.denominator * f.numerator
            F = Fraction(num, den)
            F.simplify()
            return F

    def __lt__(self, f):
        if type(f) == Fraction:
            a = self.numerator * f.denominator
            b = f.numerator * self.denominator
            if a < b:
                return True
            else:
                return False
        
    def __gt__(self, f):
        if type(f) == Fraction:
            a = self.numerator * f.denominator
            b = f.numerator * self.denominator
            if a > b:
                return True
            else:
                return False

    def __le__(self, f):
        if type(f) == Fraction:
            a = self.numerator * f.denominator
            b = f.numerator * self.denominator
            if a <= b:
                return True
            else:
                return False    

    def __ge__(self, f):
        if type(f) == Fraction:
            a = self.numerator * f.denominator
            b = f.numerator * self.denominator
            if a >= b:
                return True
            else:
                return False

    def __eq__(self, f):
        if type(f) == Fraction:
            a = self.numerator * f.denominator
            b = f.numerator * self.denominator
            if a == b:
                return True
            else:
                return False

    def __ne__(self, f):
        if type(f) == Fraction:
            a = self.numerator * f.denominator
            b = f.numerator * self.denominator
            if a != b:
                return True
            else:
                return False
        
    def __str__(self):
        return f"({self.numerator},{self.denominator})"

F1 = Fraction(2,4)
F2 = Fraction(1,6)

print(F1 + F2)
print(F1 - F2)
print(F1 * F2)
print(F1/F2)
print(F1 >= F2)
print(F1 <= F2)
print(F1 == F2)
print(F1 != F2)
