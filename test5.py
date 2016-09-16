#Count number of even and odd number
count_even=0
count_odd=0
for i in range(100):
	if i%2==0:
		count_even=count_even+1
	else:
		count_odd=count_odd+1
print("Total odd numbers = ",count_odd)
print("Total odd numbers = ",count_even)