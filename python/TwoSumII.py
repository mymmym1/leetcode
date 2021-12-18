# 167. Two Sum II - Input Array Is Sorted
# 2 <= numbers.length <= 3 * 10^4. Numbers is sorted in non-decreasing order.
def twoSum(numbers, target):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i < j and numbers[i] + numbers[j] == target:
                l = [i+1, j+1]
    return l

'''
numbers = [2,7,11,15]
target = 9

numbers = [2,3,4]
target = 6
'''
numbers = [-1,0]
target = -1

print(twoSum(numbers, target))

