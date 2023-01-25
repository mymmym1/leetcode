# 167. Two Sum II - Input Array Is Sorted
# 2 <= numbers.length <= 3 * 10^4. Numbers is sorted in non-decreasing order.
def twoSum(numbers, target):
    left = 0
    right = len(numbers) -1
    l = []
    while left < right:
        if numbers[left] + numbers[right] == target:
            l = [left + 1, right + 1]
        if numbers[left] + numbers[right] > target:
            right -= 1
        else:
            left += 1
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

