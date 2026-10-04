# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        queue = collections.deque([[root, root.val]])

        while queue:
            curr = queue.pop()
            node = curr[0]
            m = curr[1]

            if node == None:
                continue

            if node.val >= m:
                res += 1
            
            queue.append([node.left, max(node.val, m)])
            queue.append([node.right, max(node.val, m)])

        return res