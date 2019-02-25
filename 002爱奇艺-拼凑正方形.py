'''nums = list(map(int, input().strip().split()))
mi,ma = min(nums), max(nums)
total = sum(nums)
for i in range(mi, ma+1):
    if sum(map(abs,[x-i for x in nums])) < total:
        total = sum(map(abs,[x-i for x in nums]))
print(total)'''


nums = list(map(int, input().strip().split()))
nums.sort()
total = sum(nums)
for i in range(nums[1],nums[2]+1):
    if sum(map(abs,[x-i for x in nums])) < total:
        total = sum(map(abs,[x-i for x in nums]))
print(total)

arr = sorted(map(int, input().split()))
print(arr[3] + arr[2] - arr[1] - arr[0])