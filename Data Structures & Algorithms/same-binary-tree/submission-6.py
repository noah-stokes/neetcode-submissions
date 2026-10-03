# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # iterative bfs
        queue = collections.deque([[p,q]])
        res = True

        while queue:
            curr = queue.popleft()
            if curr[0] == None and curr[1] == None:
                continue
            if curr[0] == None or curr[1] == None or curr[0].val != curr[1].val:
                res = False
                break

            queue.append([curr[0].left, curr[1].left])
            queue.append([curr[0].right, curr[1].right])

        return res

