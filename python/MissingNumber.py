def missingNumber(nums):
    newset = set()
    for i in range(len(nums)+1):
        newset.add(i)
    diff = newset - set(nums)
    return diff

#nums = [3,0,1]
#nums = [0,1]
nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))