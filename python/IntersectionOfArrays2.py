def intersect(nums1, nums2):
    dic1 = {}
    result = []
    for i in nums1:
        if i not in dic1:
            dic1[i] = 1
        else:
            dic1[i] += 1
    dic2 = {}
    for i in nums2:
        if i not in dic2:
            dic2[i] = 1
        else:
            dic2[i] += 1
            
    for i in dic1.keys():
        if i in dic2.keys():
            if dic1[i] <= dic2[i]:
                n = dic1[i]
            else: n = dic2[i]
            while n > 0:
                result.append(i)
                n -= 1
    return result


#nums1 = [1, 2, 2, 1]
#nums2 = [2, 2]
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(intersect(nums1, nums2))