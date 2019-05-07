import math



class Portfolio:


	def __init__(self, expectations, variances, interest_rate=None):
		self.expectations = expectations
		self.variances = variances
		if interest_rate != None:
			self.expectations.append(lambda x: (1+interest_rate)*x)
			self.variances.append(lambda _: 0)


	# how to achieve maximal return, when you have m to invest, and your risk tolerance is given my sigma
	def max_return(self, m, sigma):
		return self.return_from(len(self.expectations), m, sigma)

	def V(self, j, x, sig_bound):
		pass

	def return_from(self, allocation):
		return (sum([self.expectations[i](allocation[i]) for i in range(len(allocation))]), sum([self.variances[i](allocation[i]) for i in range(len(allocation))]))



if __name__ == "__main__":
	my_portfolio = Portfolio(
		[lambda x: (10 * x)/(1+x), lambda x:  (math.sqrt(x)), lambda x: 10*(1 - (math.e**(-x)))],
		[lambda x: 5, lambda x: 8, lambda x: 1],
		.01
		)

	print(my_portfolio.return_from([2,1,2,5]))