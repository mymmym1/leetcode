def nextGreaterElement(nums1, nums2):
    result = []
    for i in nums1:
        for j in range(len(nums2)):
            if i == nums2[j]:
                if j == len(nums2) - 1:
                    result.append(-1)
                else:
                    if nums2[j + 1] > nums2[j]:
                        result.append(nums2[j + 1])
                    else:
                        result.append(-1)
    return result

#nums1 = [4,1,2]
#nums2 = [1,3,4,2]
nums1 = [2,4]
nums2 = [1,2,3,4]
print(nextGreaterElement(nums1, nums2))