def nextPermutation(nums):
    for i in range(len(nums)):
        if i + 1 <= len(nums) - 1:
            if nums[i + 1] - nums[i] >= 0:
                if i + 2 <= len(nums) - 1:
                    if nums[i + 2] - nums[i + 1] > 0:
                        temp = nums[i + 1]
                        nums[i + 1] = nums[i + 2]
                        nums[i + 2] = temp
                        return nums
    nums.sort()
    return nums

#nums = [1,2,3]
#nums = [3,2,1]
nums = [1,1,5]
print(nextPermutation(nums))