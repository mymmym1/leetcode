#155.Min Stack
class MinStack(object):
    def __init__(self):
        self.l = []

    def push(self, val):
        self.l.append(val)
        """
        :type val: int
        :rtype: None
        """

    def pop(self):
        if len(self.l) > 0: # None and empty
            self.l.remove(self.l[-1])
        """
        :rtype: None
        """

    def top(self):
        return self.l[-1]
        """
        :rtype: int
        """

    def getMin(self):
        return min(self.l)
        """
        :rtype: int
        """

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())
