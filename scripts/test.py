import numpy as np  
import matplotlib.pyplot as plt  
import math



functions = [None, lambda x: 10000/(1 + math.e**(-.001*(x-100)))-5000, lambda x: 1.06*x, lambda x: 20000/(1 + math.e**(-.0004*(x-100)))-11598.323]
variances = [None, lambda x: .001*x**1.7, lambda x: 0*x, lambda x: .333*x]
colors = [None, 'b', 'g', 'r']


"""
def graph(to_invest, step):  
    x = np.array(range(0, 10000, 10)) 
    plt.axis([0, 10000, -1000, 7000])
    for z in range(1, len(functions)):
    	#y = functions[z](x)
    	plt.plot(x,functions[z](x), colors[z]) 
    	plt.plot(x,variances[z](x), colors[z]) 
    plt.show()



graph(10000, 10)
"""



plt.figure(1)
x = np.array(range(0, 10000, 10))
plt.axis([0, 10000, -1000, 7000])
plt.plot(x, functions[2](x))
plt.plot(x, variances[2](x), 'r')
plt.show()




"""
plt.figure(1)

plt.subplot(311)
plt.axis([0, 10000, -1000, 7000])
plt.plot(x, functions[1](x))
plt.plot(x, variances[1](x), 'r')


plt.subplot(312)
plt.axis([0, 10000, -1000, 7000])
plt.plot(x, functions[2](x))
plt.plot(x, variances[2](x), 'r')

plt.subplot(313)
plt.axis([0, 10000, -1000, 7000])
plt.plot(x, functions[3](x))
plt.plot(x, variances[3](x), 'r')

plt.show()
"""