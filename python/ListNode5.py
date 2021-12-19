# 203. Remove Linked List Elements
#  Remove all the nodes that has Node.val == val

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class ListNode5:
    def __init__(self):
        self.head = None
    def printListNode(self):
        temp = self.head  # head can't be put in while
        while temp != None:
            print(temp.val, end=",")
            temp = temp.next

    def add(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            last = self.head
            while last.next != None:
                last = last.next
            last.next = Node(val)

def removeElements(listnode, value):
    head = listnode.head
    while head and head.val == value:
        head = head.next

    if head is None:
        return ListNode5()
    else:
        curr = head
        ll = ListNode5()
        while curr != None:
            if curr.val == value:
                if curr.next != None:
                    curr = curr.next
                else:
                    return ll
            else:
                ll.add(curr.val)
                curr = curr.next
    return ll

def convert(list):
    if len(list) == 0:
        return ListNode5()
    elif len(list) > 0:
        newlist = ListNode5()
        newlist.head = Node(list[0])
        for n in list[1:]:
            newhead = newlist.head
            while newhead.next != None:
                newhead = newhead.next
            newhead.next = Node(n)
    return newlist

list = [1,2,6,3,4,5,6]
value = 6
#list = [7, 7, 7, 7]
#value = 7
#list = []
#value = 1
listnode = convert(list)
#listnode.printListNode()
#print()
result = removeElements(listnode, value)
result.printListNode()









