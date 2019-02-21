n=int(input().strip())
nums=list(map(int,input().strip().split()))
max1 = 0
max2 = 0
max3 = 0
min1 = 0
min2 = 0
for i in nums:
	if i > max1:
		max1,max2,max3 = i, max1, max2 
	elif i > max2 and i <= max1:
		max1,max2,max3 = max1,i,max2 
	elif i > max3 and i <= max2:
		max1,max2,max3 = max1,max2,i
	elif i > min1 and i <= min2:
		min1, min2 = min1,i 
	elif i <= min1:
		min1,min2 = i, min1 

print(max(max1*max2*max3, max1*min1*min2))