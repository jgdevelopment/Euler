#primes = [0,1,2,3,0,5,0]
from math import sqrt
max_prime = int(sqrt(600851475143))
#sieve = range(max_prime)
#primes = []
bigNum = 600851475143
for x in range(2,max_prime):
#if sieve[x] != 0:
#	for i in range(x*2,max_prime,x):
#		sieve [i]=0
#	primes.append(x)
	while bigNum%x==0:
		 	if bigNum == x:
				print x
				break
			else:
				bigNum = bigNum/x

	
		