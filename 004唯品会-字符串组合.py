from functools import cmp_to_key
s = 'bac'
res = set()
l = len(s)
for i in range(l):
	for slen in range(1,l+1):
		res.add(s[i:i+slen])
res = [(i,len(i)) for i in list(res)]
def so(x, y):
	if x[1] < y[1]:
		return -1
	elif x[1] > y[1]:
		return 1
	else:
		if x[0] < y[0]:
			return -1
		elif x[0] > y[0]:
			return 1
		else:
			return 0
res = sorted(res, key = cmp_to_key(so))

re = [i[0] for i in res]
print(' '.join(re))