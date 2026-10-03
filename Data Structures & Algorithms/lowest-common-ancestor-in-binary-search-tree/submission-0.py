# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = root

        def dfs(root):
            if root == None:
                return

            nonlocal res

            if p.val < root.val and q.val < root.val:
                res = root.left
                dfs(root.left)
            elif p.val > root.val and q.val > root.val:
                res = root.right
                dfs(root.right)
        
        dfs(root)
        return res