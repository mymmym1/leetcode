# return the distinct 3rd number

def thirdMax(nums):
    numberlist = list()
    for i in nums:
        if i not in numberlist:
            numberlist.append(i)
    if len(numberlist) == 1:
        return numberlist[0]
    elif len(numberlist) == 2:
        return max(numberlist[0], numberlist[1])
    elif len(numberlist) > 2:
        return numberlist[2]
    return numberlist[0]

nums = [3,2,1]
nums = [1,2]
nums = [2,2,3,1]
print(thirdMax(nums))