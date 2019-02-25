nums = list(map(int, input().strip().split()))
nums.sort()
while True:
    if nums[2] >= nums[1] and nums[0]+nums[1] > nums[2]:
        print(sum(nums))
        break
    elif nums[2] >= nums[1] and nums[0]+nums[1] <= nums[2]:
        nums[2] -= 1
    elif nums[2] < nums[1]:
        break
