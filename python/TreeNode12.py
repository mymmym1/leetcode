# 235. Lowest Common Ancestor of a Binary Search Tree
# Binary search tree
# The number of nodes in the tree is in the range [2, 105].
# All Node.val are unique. p != q. p and q will exist in the BST.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class TreeNode12:
    def __init__(self):
        self.root = None

def lowestCommonAncestor(root, p, q):  # Recursive will not return in the middle, only returns at last.
    if root is None:
        return None
    if (root.val > p) and (root.val > q):
        return lowestCommonAncestor(root.left, p, q)
    if (root.val < p) and (root.val < q):
        return lowestCommonAncestor(root.right, p, q)
    return root

tree = TreeNode12()

tree.root = Node(6)
tree.root.left = Node(2)
tree.root.right = Node(8)
tree.root.left.left = Node(0)
tree.root.left.right = Node(4)
tree.root.right.left = Node(7)
tree.root.right.right = Node(9)
tree.root.left.right.left = Node(3)
tree.root.left.right.right = Node(5)
'''
tree.root = Node(2)
tree.root.left = Node(1)
'''

p = 2
q = 4

n = lowestCommonAncestor(tree.root, p, q)
if n:
    print(n.val)

