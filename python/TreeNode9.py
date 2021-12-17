#144. Binary Tree Preorder Traversal
#Given the root of a binary tree, return the preorder traversal of its nodes' values.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

#  Preorder (Root, Left, Right)
def preorder(n):
    if n:
        print(n.val)
        preorder(n.left)
        preorder(n.right)

tree = BinaryTree()
tree.root = Node(1)
tree.root.left = None
tree.root.right = Node(2)
tree.root.right.left = Node(3)

preorder(tree.root)



