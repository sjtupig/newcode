s = list(input())
maps = set()
res = []
for i in s:
    if i not in maps:
        maps.add(i)
        res.append(i)
print(''.join(res))
