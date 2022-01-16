# 314. Binary Tree Vertical Order Traversal (medium, Premium)
# https://goodtecher.com/leetcode-314-binary-tree-vertical-order-traversal/
# https://www.geeksforgeeks.org/print-binary-tree-vertical-order-set-2/

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class TreeNode14:
    def __init__(self):
        self.root = None

def getVerticalOrder(root, hd, m):
    if root is None:
        return
    try:
        m[hd].append(root.val)
    except:
        m[hd] = [root.val]

    getVerticalOrder(root.left, hd-1, m)
    getVerticalOrder(root.right, hd+1, m)

def printVerticalOrder(root):
    m = dict()
    hd = 0
    getVerticalOrder(root, hd, m)

    for index, value in enumerate(sorted(m)):
        for i in m[value]:
            print(i),
        print()

tree = TreeNode14()
tree.root = Node(3)
tree.root.left = Node(9)
tree.root.right = Node(20)
tree.root.right.left = Node(15)
tree.root.right.right = Node(7)

printVerticalOrder(tree.root)
