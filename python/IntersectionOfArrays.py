def intersection(nums1, nums2):
    temp = list()
    for i in nums1:
        for j in nums2:
            if i == j:
                if i not in temp:
                    temp.append(i)
    return temp

#nums1 = [1, 2, 2, 1]
#nums2 = [2, 2]
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersection(nums1, nums2))
