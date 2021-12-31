def findDisappearedNumbers(nums):
    set1 = set()
    set2 = set()
    for i in nums:
        if i not in set1:
            set1.add(i)
    for i in range(1, len(nums)+1):
        set2.add(i)
    dif = list(set2 - set1)
    return dif

nums = [4,3,2,7,8,2,3,1]
nums = [1,1]
print(findDisappearedNumbers(nums))
