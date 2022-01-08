# 1290. Convert Binary Number in a Linked List to Integer

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class ListNode9:
    def __init__(self):
        self.head = None

def getDecimalValue(listnode):
    if listnode.head is None:
        return None
    else:
        numstr = str(listnode.head.val)
        temp = listnode.head
        while temp.next is not None:
            numstr += str(temp.next.val)
            temp = temp.next
        decimalnum = int(numstr, 2)
    return decimalnum

def convert(numlist):
    if len(numlist) == 0:
        return None
    elif len(numlist) > 0:
        newlist = ListNode9()
        newlist.head = Node(numlist[0])
        for i in numlist[1:]:
            temp = newlist.head
            while temp.next:
                temp = temp.next
            temp.next = Node(i)
    return newlist

numlist = [1,0,1]
numlist = [0]
listnode = convert(numlist)
print(getDecimalValue(listnode))