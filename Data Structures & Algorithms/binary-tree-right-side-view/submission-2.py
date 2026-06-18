# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
1. Parse by level
2. Take on right most value on level

'''


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        queue = [root]
        while queue:
            level = []
            for _ in range(len(queue)):
                u = queue.pop(0)
                if u:
                    level.append(u)

                    if u.left:
                        queue.append(u.left)

                    if u.right:
                        queue.append(u.right)
            if len(level):
                res.append(level[-1].val)

        return res

        