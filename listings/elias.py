#!/usr/bin/python

from math import log,ceil

log2 = lambda x: log(x,2)

def binary(x,l=1):
	fmt = '{0:0%db}' % l
	return fmt.format(x)

def unary(x):
	return x*'1'+'0'

def elias_generic(lencoding, x):
	if x == 0: return '0'
	
	l = 1+int(log2(x))
	a = x - 2**(int(log2(x)))
	
	k = int(log2(x))

	return lencoding(l) + binary(a,k)
	
def golomb(b, x):
	q = int((x) / b)
	r = int((x) % b)
	l = int(ceil(log2(b)))

	return unary(q) + binary(r, l)
	
elias_gamma = lambda x: elias_generic(unary, x)
elias_delta = lambda x: elias_generic(elias_gamma,x)
	
for i in range(10):	
	print "%5d: %-10s : %-10s : %-10s" % \
		(i, elias_gamma(i),elias_delta(i), golomb(50,i))


