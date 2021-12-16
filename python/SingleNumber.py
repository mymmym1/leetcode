#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#You must implement a solution with a linear runtime complexity and use only constant extra space.
#(only 1 for loop and no more than one storage set or dic so on.)

def singleNumber(nums):
    s = set()
    for i in nums:
        if i in s:
            s.remove(i)
        else:
            s.add(i)
    return s.pop()

#nums = [2,2,3]
nums = [4,1,2,1,2]
#nums = [1]
print(singleNumber(nums))



