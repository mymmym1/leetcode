def containsNearbyDuplicate(nums, k):
    dic = {}
    for i in range(len(nums)):
        if nums[i] not in dic:
            dic[nums[i]] = list()
            dic[nums[i]].append(i)
        else:
            dic[nums[i]].append(i)
    for key in dic:
        for i in dic[key]:
            for j in dic[key]:
                if 0 < j-i <= k:
                    return True
    return False

nums = [1,2,3,1]
k = 3
nums = [1,0,1,1]
k = 1
nums = [1,2,3,1,2,3]
k = 2
print(containsNearbyDuplicate(nums, k))
