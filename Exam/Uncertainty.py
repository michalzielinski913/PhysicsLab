import numpy as np
import math


significant_digits=2

def significant2(number):
    return round(number, significant_digits - int(math.floor(math.log10(abs(number)))) - 1)

class Unce:

    def __init__(self):
        pass

    def addMeasurements(self, *args):
        self.measure=np.array([])
        for x in args:
            self.measure=np.append(self.measure, x)

    def averageA(self):
        return np.average(self.measure)

    def standardDevation(self):
        self.std= np.std(self.measure)
        return self.std

    def typeB(self, x):
        self.typeBB=(x/math.sqrt(3))

    def typeBP(self):
        return self.typeBB

    def studentFisher(self, value):
        self.fisher= value

    def totalUn(self):
        self.total =math.sqrt(((self.fisher**2)/3)+((self.std**2)/3))
        return self.total