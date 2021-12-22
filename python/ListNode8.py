# 237. Delete Node in a Linked List
# node to be deleted is in the list and is not a tail. The value of each node in the list is unique.
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class ListNode8:
    def __init__(self):
        self.head = None
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.val, end=',')
            temp = temp.next

    def deleteNode(self, node):
        while self.head and self.head.val == node.val:
            self.head = self.head.next
        temp = self.head
        while temp.next:
            if temp.next.val == node.val and temp.next.next != None:
                temp.next = temp.next.next
            else:
                temp = temp.next

def convert(nums):
    if len(nums) == 0:
        return None
    elif len(nums) > 0:
        listnode = ListNode8()
        listnode.head = Node(nums[0])
        for i in nums[1:]:
            temp = listnode.head
            while temp.next:
                temp = temp.next
            temp.next = Node(i)
    return listnode

nums = [4,5,1,9]
listnode = convert(nums)
#listnode.printlist()
listnode.deleteNode(Node(5))
listnode.printlist()