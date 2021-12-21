class MyQueue(object):

    def __init__(self):
        self.l = []

    def push(self, x):
        self.l.append(x)

    def pop(self):  # Removes the element from the front of the queue and returns it.
        if len(self.l) > 0:
            value = self.l[0]
            self.l.remove(self.l[0])
            return value

    def peek(self):
        if len(self.l) > 0:
            value = self.l[0]
            return value

    def empty(self):
        if len(self.l) == 0:
            return True
        else:
            return False

obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
print(obj.empty())