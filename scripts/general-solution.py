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



functions = [0, f1, f2, f3]


amounts = []

# need to cache things

cache = dict()



def V(j, x):
	if (j, x) in cache:
		print("yes")
		return cache[(j,x)]
	if j == 1:
		l = functions[j](x)
		cache[(j,x)] = l
		return l

	else:
		
		maximum = -float('inf')
		mac = 0
		for y in range(0, x):

			curr = V(j-1, x-y) + functions[j](y)  # when we recurse to the very top this will be all the way expanded out
			if curr > maximum:
				maximum = curr
				mac = y
		amounts.append(mac)
		cache[(j, x)] = maximum
		return maximum

"""
		res = max([(lambda y: (functions[j](y) + V(j-1, x-y)))(y) for y in range(0, x)])
		cache[(j, x)] = res
		return res
"""

# provides the maximum return when you have m dollars to invest among n projects
def maximal_return(m, n):
	return V(n, m)

print(V(3, 5))
print(amounts)



