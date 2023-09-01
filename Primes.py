#primes = [0,1,2,3,0,5,0]
from math import sqrt
max_Prime = int(sqrt(600851475143))
#sieve = range(max_prime)
#primes = []
big_Num = 600851475143
for x in range(2,max_Prime):
#if sieve[x] != 0:
#	for i in range(x*2,max_prime,x):
#		sieve [i]=0
#	primes.append(x)
	while big_Num%x==0:
		 	if big_Num == x:
				print x
				break
			else:
				big_Num = big_Num/x
