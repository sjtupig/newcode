from collections import Counter
s = input().strip()
k = int(input().strip())
value = sorted(Counter(s).values())
for i in range(k):
    value[-1] -= 1
    value.sort()
    

print(sum(map(lambda x:x**2, value)))