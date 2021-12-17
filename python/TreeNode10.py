#145. Binary Tree Postorder Traversal
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class TreeNode:
    def __init__(self):
        self.root = None

# Postorder (Left, Right, Root)
def postorderTraversal(n):
    if n:
        postorderTraversal(n.left)
        postorderTraversal(n.right)
        print(n.val)

tree = TreeNode()
tree.root = Node(1)
tree.root.left = None
tree.root.right = Node(2)
tree.root.right.left = Node(3)

postorderTraversal(tree.root)
