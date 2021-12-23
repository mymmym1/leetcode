# 257. Binary Tree Paths

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class TreeNode13:
    def __init__(self):
        self.root = None

def binaryTreePaths(root, path, pathLen):
    if root is None:  # root!=None; root.left!=None; root.left.left==None (return to the last line); root.left.right!=None; root.right!=None
        return
    if len(path) > pathLen:  # len(path)==pathlen==0; len(path)==pathlen==1; len(path)==pathlen==2; len(path)==pathlen==3; len(path)==3>pathlen==1
        # print("path:", path, ',', "pathLen:", pathLen, ',', "path[pathLen]:", path[pathLen])
        path[pathLen] = root.val  # ; ; ; ; path[1] = root.val=3(root.right)
        # print(path) # ; ; ; ; [1,3,5]
    else:
        path.append(root.val) # [root]; ; [root, root.left]; [root, root.left, root.left.right]
    pathLen += 1  # pathLen=1; pathLen=2; pathLen=3; pathLen=4; pathLen=2
    # print(len(path), ',', pathLen)
    if root.left is None and root.right is None:  # ; ; ; print path(pathLen=3); print path(pathLen=2)
        # print(path)
        printArray(path, pathLen)
    else:
        binaryTreePaths(root.left, path, pathLen)  # root.left (pathLen=1); root.left.left; ; root.right(poathLen=1)
        binaryTreePaths(root.right, path, pathLen) # ; ; root.left.right; ;

def printArray(ints, l):
    for i in ints[0: l]:
        print(i, "->", end="")
    print()

tree = TreeNode13()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.right = Node(5)

binaryTreePaths(tree.root, path=[], pathLen=0)

