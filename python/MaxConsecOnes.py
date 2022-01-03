def findMaxConsecutiveOnes(nums):
    count = 0
    numset = set()
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        if nums[i] == 0 or i == len(nums) - 1:
            if count not in numset:
                numset.add(count)
            count = 0
    maxones = max(numset)
    return maxones

nums = [1,1,0,1,1,1]
nums = [1,0,1,1,0,1]
print(findMaxConsecutiveOnes(nums))
