from binarytree import build

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

List = []
def rightSideView(self, root):
    if root is None:
        return 0

    RightSide = rightSideView(root.right)
    return list