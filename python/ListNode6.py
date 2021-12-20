class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
class ListNode6:
    def __init__(self):
        self.head = None
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.val, end=',')
            temp = temp.next

    def push(self, val):
        temp = Node(val)
        temp.next = self.head  # temp(Node(val)) -> self.head
        self.head = temp  # temp(Node(val)) -> self.head(temp)

def reverse(listnode):
    ll = ListNode6()
    if listnode is not None:
        curr = listnode.head
        while curr is not None:
            ll.push(curr.val)
            curr = curr.next
    return ll

def convert(num):
    if len(num) == 0:
        return None
    elif len(num) > 0:
        newlist = ListNode6()
        newlist.head = Node(num[0])
        for i in num[1:]:
            newhead = newlist.head
            while newhead.next:
                newhead = newhead.next
            newhead.next = Node(i)
    return newlist

list = [1,2,3,4,5]
#list = [1,2]
#list = []
listnode = convert(list)
newlistnode = reverse(listnode)
newlistnode.printlist()
