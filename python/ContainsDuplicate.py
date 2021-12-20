def containsDuplicate(nums):
    dic = {}
    for n in nums:
        if n not in dic:
            dic[n] = 1
        else:
            dic[n] += 1
    val_list = list(dic.values())
    for i in val_list:
        if i > 1:
            return True
    return False

nums = [1,2,3,1]
nums = [1,2,3,4]
nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums))
