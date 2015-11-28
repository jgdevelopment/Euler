sumSquare =[x**2 for x in range(101)]
squareSum =[x for x in range(101)]

total = sum(squareSum)**2

def add(a,b):
	return a+b
	
print total-reduce(add,sumSquare)

