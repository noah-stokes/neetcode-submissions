# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot == None:
            return True
        
        if root == None or subRoot == None:
            return False
        
        if root.val == subRoot.val:
            same = self.isSame(root, subRoot)
            if same:
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def isSame(self, t1, t2):
        if t1 == None and t2 == None:
            return True
        
        if t1 == None or t2 == None or t1.val != t2.val:
            return False
        
        return self.isSame(t1.left,t2.left) and self.isSame(t1.right, t2.right)
        
        
        
        