# 234. Palindrome Linked List
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class ListNode7:
    def __init__(self):
        self.head = None

    def push(self, val):
        temp = Node(val)
        temp.next = self.head
        self.head = temp
'''
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.val, end=',')
            temp = temp.next
'''

def reverse(numlist):
    reverselist = ListNode7()
    if numlist is not None:
        temp = numlist.head
        while temp is not None:
            reverselist.push(temp.val)
            temp = temp.next
    return reverselist

def isPalindrome(numlist):
    reverselist = reverse(numlist)
    temp1 = numlist.head
    temp2 = reverselist.head
    flag = True
    while temp1:
        flag = flag and (temp1.val == temp2.val)
        temp1 = temp1.next
        temp2 = temp2.next
    if flag:
        return True
    else:
        return False

def convert(nums):
    if len(nums) == 0:
        return None
    elif len(nums) > 0:
        numlist = ListNode7()
        numlist.head = Node(nums[0])
        for i in nums[1:]:
            temp = numlist.head
            while temp.next:
                temp = temp.next
            temp.next = Node(i)
    return numlist

l = [1,2,2,1]
#l = [1,2]
ll = convert(l)
#ll.printlist()
#print()
#reverse(ll).printlist()
#print()
print(isPalindrome(ll))
