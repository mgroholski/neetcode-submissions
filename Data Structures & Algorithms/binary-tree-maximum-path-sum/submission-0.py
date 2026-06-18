# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # Single 
            singleNodeVal = node.val
            leftVal = float('-inf')
            if node.left:
                leftVal = dfs(node.left)
            rightVal = float('-inf')
            if node.right:
                rightVal = dfs(node.right)

            leftPathVal = singleNodeVal + leftVal
            rightPathVal = singleNodeVal + rightVal
            
            self.maxPath = max(
                self.maxPath, 
                singleNodeVal, 
                leftPathVal, 
                rightPathVal,
                singleNodeVal + rightVal + leftVal
                )

            return max(
                singleNodeVal, 
                leftPathVal,
                rightPathVal
                )
        
        dfs(root)
        return self.maxPath
        