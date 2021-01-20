from Exam.LinearRegresion import LinearRegresion
from Exam.Uncertainty import Unce

wykres=LinearRegresion()

wykres.appendX([1, 2, 3, 4, 5, 6, 7, 8])
wykres.appendY([2, 4, 6, 8, 10, 12, 14, 16])
#Plot based on given data
wykres.defaultPlot()

#Linear regressionj calculator
wykres.generateModel()
wykres.linearPlot()
#y=mx+b
print(wykres.getM())

measure=Unce()

measure.addMeasurements([7.5, 7.4, 7.3, 7.4, 7.3])
print(measure.averageA())
print(measure.standardDevation())
measure.typeB(0.1)

print(measure.typeBP())
#https://prnt.sc/wnfzri mnożymy średnią razy wartość w tabelce, tabelka niezaimplementowana musisz samemu
measure.studentFisher(0.77)
print(measure.totalUn())

