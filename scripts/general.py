import math


INTEREST_RATE = .02


def f1(x):
	return (10 * x)/(1+x)
def f2(x):
	return (math.sqrt(x))
def f3(x):
	return 10*(1 - (math.e**(-x)))

# depositing in bank
def f4(x):
	return (1+INTEREST_RATE)*x

def g1(x):
	return -3*x
def g2(x):
	return -1*x
def g3(x):
	return -3*x

functions = [0, f1, f2, f3, f4]


amounts = []

# need to cache things

cache = dict()

# at each stage return/cache how we got there
def V(j, x):

	if (j, x) in cache:
		return cache[(j,x)]
	
	if j == 1:
		cache[(j,x)] = (functions[j](x), [x])
		return cache[(j,x)]

	else:
		maximum = (-float('inf'), None)
		mac = 0
		for y in range(0, x):
			temp = V(j-1, x-y) 
			curr = (temp[0] + functions[j](y), temp[1].copy())
			if curr > maximum:
				maximum = curr 
				mac = y

		maximum[1].append(mac)
		cache[(j, x)] = maximum
		return cache[(j,x)]
"""
		res = max([(lambda y: (functions[j](y) + V(j-1, x-y)))(y) for y in range(0, x)])
		cache[(j, x)] = res
		return res
"""

# provides the maximum return when you have m dollars to invest among n projects
def maximal_return(m, n):
	global cache
	cache = dict()
	return V(n, m)

print(V(3, 5))
print(V(3, 5))


#print(sum([f1(2), f2(1), f3(2)]))
#print(sum([f1(5), f2(2), f3(3)]))



# m * (n+1)