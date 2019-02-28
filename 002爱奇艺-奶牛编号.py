n = int(input().strip())
nums = list(map(int, input().strip().split(' ')))
nums.sort()
res = 1
for i,v in enumerate(nums):
    res = ((res%1000000007)*((v-i)%1000000007)) % 1000000007
print(res)