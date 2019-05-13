import math


class Portfolio:

	# Creates a suite of investment projects with provided expected return functions and variance functions.
	# If interest rate is defined, then we add a risk free function with return f(x) = (1+r)*x
	def __init__(self, expectations, variances, interest_rate=None):
		if len(expectations) != len(variances):
			raise ValueError("expectations must be same length as variances")
		self.expectations = expectations
		self.variances = variances



	# how to achieve maximal return, when you have m to invest, and your risk tolerance is given my sigma
	def max_return(self, m, sigma):
		self.cache = dict()
		if m < 0:
			raise ValueError("cannot invest a negative amount")
		return self.V(len(self.expectations)-1, m, sigma)

	# recursive helper
	def V(self, j, x, sigma):
		if (j, x, sigma) in self.cache:
			return self.cache[(j, x, sigma)]
		
		elif sigma < 0:
			return (-float('inf'), 0, [x])

		elif j == 1:
			if sigma - self.variances[j](x) >= 0:
				self.cache[(j, x, sigma)] = (self.expectations[j](x), self.variances[j](x), [x])
				return self.cache[(j, x, sigma)]
			else:
				return (-float('inf'), 0, [x])
		else:
			maximum = (-float('inf'), 0, [x])
			max_allocation = None
			for y in range(0, x, 3):
				if sigma-self.variances[j](y) >= 0:
					temp = self.V(j-1, x-y, sigma-self.variances[j](y))
					curr = (temp[0] + self.expectations[j](y), temp[1] + self.variances[j](y), temp[2])
					if curr > maximum:
						maximum = curr
						max_allocation = y

			maximum = (maximum[0], maximum[1], maximum[2].copy())
			maximum[2].append(max_allocation)
			if maximum[0] != -float('inf'):
				self.cache[(j, x, sigma)] = maximum
			return maximum




### Driver Code ###
if __name__ == "__main__":
	rw = Portfolio(
		[None, lambda x: 10000/(1 + math.e**(-.001*(x-100)))-5000, lambda x: 1.06*x, lambda x: 20000/(1 + math.e**(-.0004*(x-100)))-11600],
		[None, lambda x: .001*x**1.7, lambda x: 0, lambda x: .333*x]
		)

	print(rw.max_return(10000, 1500))
	print(rw.max_return(10000, 500))
	print(rw.max_return(10000, float('inf')))
