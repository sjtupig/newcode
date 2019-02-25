from collections import Counter
s = input().strip()
t = Counter(s)
res = min(t.values())
for i in range(1,len(s)-1):
    tleft = Counter(s[:i])
    tright = Counter(s[i:])
    if tleft['G']+tright['R'] < res:
        res = tleft['G']+tright['R']
print(res)