#!/usr/bin/env python

"""Calculate binomial coefficients."""

from math import log, factorial
import doctest
import argparse

def parse_args():
	"""Parse script arguments"""
	parser = argparse.ArgumentParser()
	parser.add_argument("-n", type=int, help="total number of items to choose from")
	parser.add_argument("-k", type=int, help="number of items to choose")
	parser.add_argument("-l", "--log", action="store_true", help="returns the log binomial coefficient")
	parser.add_argument("--test", action="store_true", help="tests the module and quits")
	return parser.parse_args()

def logfactorial(n, k=0):
	"""Return log(n!) for any integer n>0, such that
	log(n!/k!) = log((k+1)*...*n) = log(k+1) + ... + log(n)

	>>> logfactorial(1, 5)
	0.0
	>>> logfactorial(5, 5)
	0
	>>> logfactorial(5, 4)
	1.6094379124341003
	>>> logfactorial(5, 6)
	0.0
	"""
	# preconditions: n, k should be non-negative integers
	assert isinstance(n, int), "n should be an integer"
	assert n >= 0, "n should be non-negative"
	assert isinstance(k, int), "k should be an integer"
	assert k >= 0, "k should be non-negative"
	# sum of zero terms
	if k > n:
		return log(1)
	return sum(log(i) for i in range(k+1, n+1))

def choose(n, k=0, log=False):
	"""Calculate log of binomial: log(choose(n,k)) 
	for any integers n >= 0 and 0 <= k <= n
	If coeff is True, return the binomial coefficient 
	itself as an integer; otherwise, return its log
	as a float.

	>>> choose(150, 40, False)
	4408904561912224983184438531922899800L
	>>> choose(1500, 400, True)
	866.1129352492226
	>>> choose(100, 30, False)
	29372339821610944823963760L
	>>> choose(1000, 300, True)
	607.2714962643722
	"""
	if log:
		return logfactorial(n, k) - logfactorial(n-k)
	else:
		return factorial(n) / (factorial(k)*factorial(n-k))

if __name__ == "__main__":
	# get args
	args = parse_args()
	# run tests
	if args.test:
		print("testing the module...")
		doctest.testmod()
		print("done with tests")
	# display calculation
	else:
		print(choose(n=args.n, k=args.k, log=args.log))