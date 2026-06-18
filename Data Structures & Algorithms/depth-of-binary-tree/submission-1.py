# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 1
        stack = [(root, 1)]
        while stack:
            n, dist = stack.pop(0)

            res = max(res, dist)

            if n.left:
                stack.append((n.left, dist + 1))

            if n.right:
                stack.append((n.right, dist + 1))

        return res


        