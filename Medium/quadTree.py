# 427. Construct Quad Tree

class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):  # boolean val = 0 (False) or 1 (True)
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


def construct(grid):  #grid: List[List[int]]
    if not grid:
        return None
    def dfs(grid, x, y, l):  # x: matrix vertical axis, y: matrix horizontal axis, (0,0) point is the upper left point.
        if l == 1:  # 1 number in 1 cell of a 4-cell grid structure
            return Node(grid[x][y] == 1, True, None, None, None, None)
        half = l // 2  # when l > 1, e.g. l = 2
        topLeftNode = dfs(grid, x, y, half)
        topRightNode = dfs(grid, x, y+half, half)
        bottomLeftNode = dfs(grid, x+half, y, half)
        bottomRightNode = dfs(grid, x+half, y+half, half)
        if topLeftNode.isLeaf and topRightNode.isLeaf and bottomLeftNode.isLeaf and bottomRightNode.isLeaf \
            and topLeftNode.val == topRightNode.val == bottomLeftNode.val == bottomRightNode.val:
            return Node(topLeftNode.val, True, None, None, None, None) # is leaf: a grid with cell numbers all the same.
        return Node(True, False, topLeftNode, topRightNode, bottomLeftNode, bottomRightNode)  # is not leaf: a grid with different cell numbers
    return dfs(grid, 0, 0, len(grid))  # rtype: Node

# To print the result:
def aNode(node):  # sublist
    if node:
        return [int(node.isLeaf), int(node.val)]
    else:
        return None

def pprintQTree2(tree):
    res = []  # list of list
    if tree:
        res.append(aNode(tree))
        res.append(aNode(tree.topLeft))
        res.append(aNode(tree.topRight))
        res.append(aNode(tree.bottomLeft))
        res.append(aNode(tree.bottomRight))
        for n in [tree.topLeft, tree.topRight, tree.bottomLeft, tree.bottomRight]:
            if n.isLeaf:
                res.extend([None, None, None, None])  # add a list to a list
            else:
                res.append(aNode(n.topLeft))
                res.append(aNode(n.topRight))
                res.append(aNode(n.bottomLeft))
                res.append(aNode(n.bottomRight))
    while res[-1] is None:  # remove nulls at the end of the list, which are all leaves
        res.pop()
    return res

grid = [[0,1],[1,0]]
node = construct(grid)
# print(node.isLeaf, node.val, node.topLeft.isLeaf, node.topLeft.val, node.topRight.isLeaf,  node.topRight.val, node.bottomLeft.isLeaf, node.bottomLeft.val, node.bottomRight.isLeaf, node.bottomRight.val)

# grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
# node = construct(grid)

print(pprintQTree2(node))