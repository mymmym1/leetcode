# 225. Implement Stack using Queues
class MyStack(object):

    def __init__(self):
        self.l = []

    def push(self, x):
        self.l.append(x)

    def pop(self):
        if len(self.l) > 0:
            value = self.l[-1]
            self.l.remove(self.l[-1])
            return value
        """
        :rtype: int
        """

    def top(self):
        if len(self.l) > 0:
            return self.l[-1]

    def empty(self):
        if len(self.l) > 0:
            return False
        else:
            return True
        """
        :rtype: bool
        """

obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())
print(obj.pop())
print(obj.empty())