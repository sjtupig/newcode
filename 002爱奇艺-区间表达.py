n = int(input().strip())
nums = list(map(int, input().strip().split()))
res = 1
for i in range(n-1):
    if nums[i+1] != nums[i]+1:
        res += 1
print(res)