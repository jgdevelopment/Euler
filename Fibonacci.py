first = 1
next = 2
holder = next
fibs =[]
for x in range(40):
	next = first+next
	first = holder
	holder = next
	
	fibs.append(first)
	fibs.append(next)
	
for i in range ((int)fibs):
	sum = fibs[i]+fibs[i-1]

print sum