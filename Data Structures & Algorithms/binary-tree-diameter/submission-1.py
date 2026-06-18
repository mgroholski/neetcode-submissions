# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0
        def dfs(n):
            nonlocal res

            leftScore = 0
            if n.left:
                leftScore = dfs(n.left) + 1

            rightScore = 0
            if n.right:
                rightScore = dfs(n.right) + 1

            res = max(res, rightScore + leftScore)
            return max(rightScore, leftScore)

            
        dfs(root)
        return res