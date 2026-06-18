# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
We can check that the current node val is within the range

Every time we go left we ristrict the upper limit
Every time we go right we restrict the lower limit
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(u, lower, upper):
            if not (lower < u.val < upper):
                return False

            leftValid = True
            if u.left:
                leftValid = dfs(u.left, lower, u.val)

            rightValid = True
            if u.right:
                rightValid = dfs(u.right, u.val, upper)

            return leftValid and rightValid

        return dfs(root, float('-inf'), float('inf'))



        