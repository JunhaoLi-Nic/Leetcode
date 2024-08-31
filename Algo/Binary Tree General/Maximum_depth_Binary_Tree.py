from binarytree import tree, bst, heap

class Node:
    def __init__(self, val=0, left=None, right=None):
     self.val = val
     self.left = left
     self.right = right

def maxDepth(root) -> int:
    if root == None:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return 1 + max(left_depth, right_depth)

#root = [3,9,20,None,None,15,7]
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

print(maxDepth(root))