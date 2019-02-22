s = input().strip()
l = len(s)
slen = 0
for i in range(l-1,0,-1):
	if s[:i] == s[-i:]:
		slen = i
		break 
print(s+s[slen:])