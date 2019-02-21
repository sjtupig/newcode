s = list(input())
maps = set()
res = []
for i in s:
    if i not in maps:
        maps.add(i)
        res.append(i)
print(''.join(res))


#


s = raw_input()
res = ''
for string in s :
    if string not in res :
        res = res + string
print(res)
