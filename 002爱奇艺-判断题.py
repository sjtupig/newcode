nums = list(map(int,input().strip().split(' ')))

print(min(nums[1],nums[2])+min(nums[0]-nums[1],nums[0]-nums[2]))