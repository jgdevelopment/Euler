x = 1
done = False
while not done:
	done = True
	x+=1
	for y in range (20):
		if x%(y+1) !=0:
			done = False
			break
	
print x