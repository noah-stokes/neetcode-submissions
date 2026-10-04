# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = collections.deque([[root, [float('-inf'), float('inf')]]])

        while queue:
            curr = queue.pop()
            node = curr[0]
            rng = curr[1]

            if node == None:
                continue

            if not (node.val > rng[0] and node.val < rng[1]):
                return False
            
            queue.append([node.left, [rng[0], node.val]])
            queue.append([node.right, [node.val, rng[1]]])
        
        return True




