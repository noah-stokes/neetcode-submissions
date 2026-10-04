# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
         res = root

         stack = [root]

         while stack:
            curr = stack.pop()
            if curr == None:
                continue
            
            if p.val < curr.val and q.val < curr.val:
                res = curr.left
                stack.append(curr.left)
            elif p.val > curr.val and q.val > curr.val:
                res = curr.right
                stack.append(curr.right)
        
         return res
        