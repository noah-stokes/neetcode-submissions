# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        elif root.right and root.left:
            return 1 + max(self.maxDepth(root.left),
                self.maxDepth(root.right))
        elif root.right:
            return 1 + self.maxDepth(root.right)
        elif root.left:
            return 1 + self.maxDepth(root.left)
        else:
            return 1