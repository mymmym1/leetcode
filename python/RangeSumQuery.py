class NumArray(object):

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        sum = 0
        for i in range(left, right+1):
            sum += self.nums[i]
        return sum

nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
left = 0
right = 5
print(obj.sumRange(left,right))