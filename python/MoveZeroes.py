# You must do this in-place without making a copy of the array.
class MoveZeros:
    def moveZeroes(self, nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                while i < len(nums) - 1:
                    temp = nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1] = temp
                    i += 1
        print(nums)

m = MoveZeros()
nums = [0,1,0,3,12]
#nums = [0]
m.moveZeroes(nums)