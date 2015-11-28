place_1 =0
place_2 =1
place_3 =0
sumOfAll = 0

while place_3 in range(4*10**6):
	place_1 = place_2
	place_2 = place_3
	place_3 = place_1+place_2
	if place_3%2==0:
		sumOfAll = place_3+sumOfAll
print sumOfAll
		
