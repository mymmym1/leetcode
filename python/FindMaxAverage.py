# You are given an integer array nums consisting of n elements, and an integer k. 
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
def findMaxAverage(nums, k):  #[nums,k)
    curr = 0.0
    for i in range(k):
        curr += nums[i]
    ans = curr
    for i in range(k, len(nums)):   #[k,len(nums))
        curr += nums[i] - nums[i - k]        
        ans = max(ans, curr)
    return ans / k
        
      
