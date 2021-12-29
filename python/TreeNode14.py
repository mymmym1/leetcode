# 404. Sum of Left Leaves
# The number of nodes in the tree is in the range [1, 1000].

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class TreeNode14:
    def __init__(self):
        self.root = None

def sumOfLeftLeaves(root):
    if root is None:  # Must determine
        return 0
    else:
        if root.left:  # Must determine root.left is not None
            return(root.left.val + sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right))
            # Display Fibonacci Sequence using Recursive:
            # https://www.programiz.com/python-programming/examples/fibonacci-recursion
    return 0

tree = TreeNode14()

tree.root = Node(3)
tree.root.left = Node(9)
tree.root.right = Node(20)
tree.root.right.left = Node(15)
tree.root.right.right = Node(7)
'''
tree.root = Node(1)
'''

print(sumOfLeftLeaves(tree.root))