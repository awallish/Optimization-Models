import math

INTEREST_RATE = .02
TOLERANCE = .80



def m1(x):
	return (10 * x)/(1+x)
def m2(x):
	return (math.sqrt(x))
def m3(x):
	return 10*(1 - (math.e**(-x)))
def m4(x):
	return (1+INTEREST_RATE)*x

def s1(x):
	pass
def s2(x):
	pass
def s3(x):
	pass
def s4(x):
	0




expectations = [0, m1, m2, m3, m4]
variances = [0, s1, s2, s3, s4]



def V(j, x):
