import matplotlib.pyplot as plt
from pylab import mpl

x = [50, 100, 144]
y = [10, 12, 16]
 
def ParametersOfLagrangeInterpolation(data_x,data_y,size):
    parameters=[]
         #i используется для управления количеством параметров
    i=0
    while i < size:
                 #jПеременная, используемая для управления циклом, умножается
        j = 0
        temp = 1
        while j < size:
            if(i != j):
                temp*=data_x[i]-data_x[j]
            j+=1
        parameters.append(data_y[i]/temp)
        i += 1
    return parameters
 
def CalculateTheValueOfLarangeInterpolation(data_x,parameters,x):
    returnValue=0
    i = 0
    while i < len(parameters):
        temp = 1
        j = 0
        while j< len(parameters):
            if(i!=j):
                temp *=x-data_x[j]
            j+=1
        returnValue += temp * parameters[i]
        i += 1
    return returnValue
 

def  Draw(data_x,data_y,new_data_x,new_data_y):
        plt.plot (new_data_x, new_data_y, label = "соответствующая кривая", color = "black")
        plt.scatter (data_x, data_y, label = "дискретные данные", color = "red")
        plt.scatter (120.999, 13.6527, label = "real data", color = "green")
        mpl.rcParams['axes.unicode_minus'] = False
        plt.title ("Данные подгонки лагранжевой интерполяции")
        plt.legend(loc="upper left")
        plt.grid(True)
        plt.show()
 
parameters=ParametersOfLagrangeInterpolation(x,y,3)
datax=[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]
datay=[]
for temp in datax:
    datay.append(CalculateTheValueOfLarangeInterpolation(x,parameters,temp))
x.append(120.999)
y.append(CalculateTheValueOfLarangeInterpolation(x,parameters,120.999))
Draw(x,y,datax,datay)