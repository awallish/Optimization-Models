import math



# since we don't clear the cache between calls, if any of the class data is updated, 
# we need to clear cache then.
class Portfolio:

	# Creates a suite of investment projects with provided expected return functions and variance functions.
	# If interest rate is defined, then we add a risk free function with return f(x) = (1+r)*x
	def __init__(self, expectations, variances, interest_rate=None):
		if len(expectations) != len(variances):
			raise ValueError("expectations must be same length as variances")
		self.expectations = expectations
		self.variances = variances
		self.cache = dict()
		if interest_rate != None:
			self.expectations.append(lambda x: (1+interest_rate)*x)
			self.variances.append(lambda _: 0)


	# how to achieve maximal return, when you have m to invest, and your risk tolerance is given my sigma
	def max_return(self, m, sigma):
		self.cache = dict()
		if m < 0:
			raise ValueError("cannot invest a negative amount")
		return self.V(len(self.expectations)-1, m, sigma)

	# recursive helper
	def V(self, j, x, sigma):
		if sigma < 0:
			return (-float('inf'), 0, [x])
		elif (j, x) in self.cache:
			return self.cache[(j, x)]
		elif j == 1:
			if sigma - self.variances[j](x) >= 0:
				self.cache[(j, x)] = (self.expectations[j](x), self.variances[j](x), [x])
				return self.cache[(j, x)]
			else:
				return (-float('inf'), 0, [x])
		else:
			maximum = (-float('inf'), 0, [x])
			max_allocation = None
			for y in range(0, x+1):
				temp = self.V(j-1, x-y, sigma-self.variances[j](y))
				curr = (temp[0] + self.expectations[j](y), temp[1] + self.variances[j](y), temp[2].copy())
				if curr > maximum:
					maximum = curr
					max_allocation = y

			maximum[2].append(max_allocation)
			self.cache[(j, x)] = maximum
			return self.cache[(j, x)]

	# returns a tuple of the expected maximum return, and the variance
	# allocation must be equal in length to expectations and variances
	def return_from(self, allocation):
		if len(allocation) != len(self.expectations):
			raise ValueError("must allocate an amount to each investment project")
		return (sum([self.expectations[i](allocation[i]) for i in range(1, len(allocation))]), sum([self.variances[i](allocation[i]) for i in range(1, len(allocation))]))






if __name__ == "__main__":
	my_portfolio = Portfolio(
		[None, lambda x: (10 * x)/(1+x), lambda x:  (math.sqrt(x)), lambda x: 10*(1 - (math.e**(-x)))],
		[None, lambda x: 2*x, lambda x: 8*x, lambda x: 1*x],
		#.01
		)

	print(my_portfolio.return_from([None, 0,0,5]))
	print(my_portfolio.max_return(5, 9))
	print(my_portfolio.max_return(5, 10))
	print(my_portfolio.max_return(5, 14))
	print(my_portfolio.max_return(5, 6)) 
	print(my_portfolio.max_return(5, 5)) # issue here still
