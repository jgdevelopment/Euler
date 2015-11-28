from math import sqrt

def getPrimes(max_prime):
	sieve = range(max_prime)
	primes = []
	for x in range(2,max_prime):
		if sieve[x] != 0:
			for i in range(x*2,max_prime,x):
				sieve [i]=0
			primes.append(x)
	return primes
	
