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
		self.count = 0
		self.cache_hits = 0
		self.cache = dict()
		if m < 0:
			raise ValueError("cannot invest a negative amount")
		return self.V(len(self.expectations)-1, m, sigma)

	# recursive helper
	def V(self, j, x, sigma):
		if (j, x, sigma) in self.cache:
			self.cache_hits += 1
			return self.cache[(j, x, sigma)]
		
		elif sigma < 0:
			self.count += 1
			return (-float('inf'), 0, [x])

		elif j == 1:
			self.count += 1
			if sigma - self.variances[j](x) >= 0:
				self.cache[(j, x, sigma)] = (self.expectations[j](x), self.variances[j](x), [x])
				return self.cache[(j, x, sigma)]
			else:
				return (-float('inf'), 0, [x])
		else:
			self.count += 1
			maximum = (-float('inf'), 0, [x])
			max_allocation = None
			for y in range(0, x+1):
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

	# returns a tuple of the expected maximum return, and the variance
	# allocation must be equal in length to expectations and variances
	def return_from(self, allocation):
		if len(allocation) != len(self.expectations):
			raise ValueError("must allocate an amount to each investment project")
		return (sum([self.expectations[i](allocation[i]) for i in range(1, len(allocation))]), sum([self.variances[i](allocation[i]) for i in range(1, len(allocation))]))


	def graph_returns():
		pass


	# how to achieve maximal return, when you have m to invest, and your risk tolerance is given my sigma
	def ax_return(self, m, sigma):
		self.count = 0
		self.cache_hits = 0
		self.cache = dict()
		if m < 0:
			raise ValueError("cannot invest a negative amount")
		return self.V(len(self.expectations)-1, m, sigma)

	# recursive helper
	def V(self, j, x, sigma):
		if (j, x) in self.cache:
			self.cache_hits += 1
			return self.cache[(j, x)]
		
		elif sigma < 0:
			self.count += 1
			return (-float('inf'), 0, [x])

		elif j == 1:
			self.count += 1
			if sigma - self.variances[j](x) >= 0:
				self.cache[(j, x)] = (self.expectations[j](x), self.variances[j](x), [x])
				return self.cache[(j, x)]
			else:
				return (-float('inf'), 0, [x])
		else:
			self.count += 1
			maximum = (-float('inf'), 0, [x])
			max_allocation = None
			for y in range(0, x+1):
				if sigma-self.variances[j](y) >= 0:
					temp = self.V(j-1, x-y, sigma-self.variances[j](y))
					curr = (temp[0] + self.expectations[j](y), temp[1] + self.variances[j](y), temp[2])
					if curr > maximum:
						maximum = curr
						max_allocation = y

			maximum = (maximum[0], maximum[1], maximum[2].copy())
			maximum[2].append(max_allocation)
			if maximum[0] != -float('inf'):
				self.cache[(j, x)] = maximum
			return maximum




if __name__ == "__main__":
	my_portfolio = Portfolio(
		[None, lambda x: 5/2*x ,lambda x: (10 * x)/(1+x), lambda x:  (math.sqrt(x)), lambda x: 10*(1 - (math.e**(-x)))],
		[None, lambda x: 1*x, lambda x: 2*x, lambda x: 8*x, lambda x: 1*x],
		.01
		)


	#print(my_portfolio.max_return(5, 9))
	#print(my_portfolio.max_return(5, 10))
	#print(my_portfolio.max_return(5, 14))
	#print(my_portfolio.max_return(5, 6)) 
	#print(my_portfolio.max_return(5, 5))
	#print(my_portfolio.max_return(5, 0))

	print(my_portfolio.ax_return(10, 1000000))
	print(my_portfolio.count, my_portfolio.cache_hits)
	print(my_portfolio.ax_return(100, 1000000))
	print(my_portfolio.count, my_portfolio.cache_hits)
	print(my_portfolio.ax_return(1000, 1000000))
	print(my_portfolio.count, my_portfolio.cache_hits)
	#print(my_portfolio.max_return(10000, 1000000))
	#print(my_portfolio.count)
