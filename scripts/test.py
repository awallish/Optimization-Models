import numpy as np  
import matplotlib.pyplot as plt  
import math



functions = [None, lambda x: 10000/(1 + math.e**(-.001*(x-100)))-5000, lambda x: 1.06*x, lambda x: 20000/(1 + math.e**(-.0004*(x-100)))-11598.323]



def graph(to_invest, step):  
    x = np.array(range(0, 10000, 10)) 
    plt.axis([0, 10000, 0, 7000])
    for z in range(1, len(functions)):
    	y = functions[z](x)
    	plt.plot(x,y) 
    plt.show()  



graph(10000, 10)