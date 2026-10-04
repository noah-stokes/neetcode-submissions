# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = {}

        queue = collections.deque([[root, 0]])

        while queue:
            curr = queue.popleft()

            if curr[0] == None:
                continue

            if curr[1] not in levels:
                levels[curr[1]] = []
            levels[curr[1]].append(curr[0].val)
            
            queue.append([curr[0].left, 1 + curr[1]])
            queue.append([curr[0].right, 1 + curr[1]])

        return list(levels.values())
