# nums: sorted unique integer array
def summaryRanges(nums):
    if len(nums) == 0:
        print("[]")
    else:
        newi = 0
        for i in range(len(nums)):  # i=0; i=1; i=2
            if newi > i:  # ; ; 2 = 2
                if newi + 1 < len(nums):
                    i = newi + 1
                else:
                    break
            elif newi == i and newi == len(nums) - 1:
                break
            head = nums[i]  # head=nums[0]=0; head=nums[1]=2
                # i+1<len(nums): # 1<3; 2<3
            while i+1 < len(nums) and nums[i+1]-nums[i] == 1:  # nums[1]-nums[0]=2; nums[2]-nums[1]=1
                i += 1  # ; i=2
            tail = nums[i]  # tail=nums[0]=0; tail=nums[2]=3
            newi = i  # newi=0; newi=2
            if head == tail:
                print(head, end=',')
            else:
                print(head, '->', tail, end=',')

#nums = [0,1,2,4,5,7]
nums = [0,2,3,4,6,8,9]
summaryRanges(nums)
