#141. Linked List Cycle
#A loop may exist in a list connecting the "tail" to any position(pos) in the list. pos is a known input.
#Write a program to research if a loop exists.
#The number of the nodes in the list is in the range [0, 10^4].

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def has_cycle(self):
        s = set()
        temp = self.head
        while temp:
            if temp in s:
                return True
            s.add(temp)
            temp = temp.next
        return False

#Make a cycle from an input list.
    def get_node(self, pos):  #pos is the loop pointed position.
        if pos != -1:
            p = 0
            tmp = self.head
            while p < pos:
                tmp = tmp.next
                p += 1  #jump out of loop when p=pos
            return tmp
    def make_cycle(self, pos):
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = self.get_node(pos) #Connect the found tail to the loop pointed position.

#Print out the list.
    def printListNode(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next

#Convert an input list into listNode.
def convert(nums):
    if len(nums) == 0:
        return None
    elif len(nums) > 0:
        myll = LinkedList()
        myll.head = Node(nums[0])
        for i in nums[1:]:      #If there is only one element, i will be None.
            ptr = myll.head
            while ptr.next:     #Assign all values with a loop.
                ptr = ptr.next
            ptr.next = Node(i)  #Assign value i to the Node(none) after tail.
        return myll

nums = [3,2,0,-4]
nums = [1, 2]
nums = [1]
ll = convert(nums)
ll.printListNode()

# ll.make_cycle(pos=1)
# ll.make_cycle(pos=0)
ll.make_cycle(pos=-1)
has = ll.has_cycle()
print(has)





