#n,s = map(int,input().strip().split(" "))
t = list(map(int, input().strip().split(' ')))
f = list(map(int, input().strip().split(' ')))
n, s = t[0], t[1]
res = 0
used = 0
for i in f:
    if used + i <= s:
        res+=1
        used+=i 
    else:
        break
print(res)
'''
for i in f:
    if used + i <= s:
        res+=1
        used+=i 
    else:
    	print(res)
        break
这么写的话，当燃油足够所有飞行的时候是没有输出值的。注意把返回值放到整个遍历之后

'''