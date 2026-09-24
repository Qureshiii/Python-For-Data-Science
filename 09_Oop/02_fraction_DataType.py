# 3/4 * 1/2 it gives the answer in 0.375

class Fraction:
    
    # this is called parameterized constructor
    def __init__(self,x,y):
        
        self.numerator = x
        self.denumerator = y
        
    def __str__(self):
        
        return '{}/{}'.format(self.numerator,self.denumerator)

    def __add__(self,other):
        
        new_num = self.numerator*other.denumerator + other.numerator*self.denumerator
        new_den = self.denumerator*other.denumerator
        
        return '{}/{}'.format(new_num,new_den)

    def __sub__(self,other):
        
        new_num = self.numerator*other.denumerator - other.numerator*self.denumerator
        new_den = self.denumerator*other.denumerator
        
        return '{}/{}'.format(new_num,new_den)

    def __mul__(self,other):
        
        new_num = self.numerator*other.numerator 
        new_den = self.denumerator*other.denumerator
        
        return '{}/{}'.format(new_num,new_den)


    def __truediv__(self, other):
        
        new_num = self.numerator*other.denumerator 
        new_den = self.denumerator*other.numerator
        
        return '{}/{}'.format(new_num,new_den)

    # convert from fraction to decimal
    def convert_to_decimal(self):
        return self.numerator / self.denumerator


fr1 = Fraction(3,4)
fr2 = Fraction(1,2)
print(fr1 + fr2)
print(fr1 - fr2)
print(fr1 * fr2)
print(fr1 / fr2)

print(fr1.convert_to_decimal())