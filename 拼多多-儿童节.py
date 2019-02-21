n1 = int(input().strip())
h = list(map(int, input().strip().split(' ')))
n2 = int(input().strip())
w = list(map(int, input().strip().split(' ')))
i,j = 0,0
res = 0
h.sort()
w.sort()
while i<n1 and j<n2:
    if h[i] > w[j]:
        j+=1
    else:
        i+=1
        j+=1
        res+=1
    '''
    if h[i] > w[j]:
        j+=1
    if h[i] <= w[j]:
        i+=1
        j+=1
        res+=1
    这么写就会有问题，因为第一个if结束后，如果j+1后j==n2，那么下一句就会越界
    '''
print(res)