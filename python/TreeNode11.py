# 226. Invert Binary Tree
# Given the root of a binary tree, invert the tree, and return its root.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class TreeNode11:
    def __init__(self):
        self.root = None

# invert binary tree
def invert(root):
    if not root:
        return
    temp = root.left
    root.left = root.right
    root.right = temp
    invert(root.left)
    invert(root.right)
    return root

# print level by level
def height(root):
    if root is None:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

def printCurLevel(root, level):
    if root != None:
        if level == 1:
            print(root.val, end=",")
        elif level > 1:
            printCurLevel(root.left, level - 1)
            printCurLevel(root.right, level - 1)

def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printCurLevel(root, i)

tree = TreeNode11()

tree.root = Node(4)
tree.root.left = Node(2)
tree.root.right = Node(7)
tree.root.left.left = Node(1)
tree.root.left.right = Node(3)
tree.root.right.left = Node(6)
tree.root.right.right = Node(9)
'''
tree.root = Node(2)
tree.root.left = Node(1)
tree.root.right = Node(3)
'''
printLevelOrder(tree.root)
print()
printLevelOrder(invert(tree.root))
