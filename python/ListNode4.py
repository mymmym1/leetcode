# 160. Intersection of Two Linked Lists
# Given the heads of two singly linked-lists headA and headB, return value of the node at which the two lists intersect.
# listA and listB's length >= 1. If listA and listB do not intersect, return null.
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class ListNode:
    def __init__(self):
        self.head = None

def getIntersectionNode(listnodeA, listnodeB):
    s = set()
    currA = listnodeA.head
    currB = listnodeB.head
    while currA:
        s.add(currA)
        currA = currA.next
    while currB:
        if currB in s:
            return currB
        currB = currB.next
    return None

llA = ListNode()
llB = ListNode()
'''
llA.head = Node(4)
llB.head = Node(5)
intersect = Node(8, Node(4, Node(5)))
llA.head.next = Node(1, intersect)
llB.head.next = Node(6, Node(1, intersect))

llA.head = Node(1)
llB.head = Node(3)
intersect = Node(2, Node(4))
llA.head.next = Node(9, Node(1, intersect))
llB.head.next = Node(3, intersect)
'''
llA.head = Node(2)
llB.head = Node(1)
llA.head.next = Node(6, Node(4))
llB.head.next = Node(5)

n = getIntersectionNode(llA, llB)
if n == None:
    print("null")
else:
    print("Intersected at ", n.val)
