# Data Structures and Algorithms Crash Course
# Minimum Value to Get Positive Step by Step Sum

class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0] >= 0:
            ans = 1
        else:
            ans = 1 - nums[0]        
        prefix = [ans + nums[0]]
            
        for i in range(1, len(nums)):
            if prefix[-1] + nums[i] > 0:
                prefix.append(prefix[-1] + nums[i])
            else: 
                ans += 1 - (prefix[-1] + nums[i])               
                prefix.append(1)
        return ans
