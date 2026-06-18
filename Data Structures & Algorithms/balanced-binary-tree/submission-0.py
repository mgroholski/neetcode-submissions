# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> int:
        self.balanced = True

        def dfs(curr) -> int:
            if not curr:
                return 0

            leftVal = dfs(curr.left)
            rightVal = dfs(curr.right)
            
            if abs(rightVal - leftVal) > 1:
                self.balanced = False
            
            return max(leftVal, rightVal) + 1

        dfs(root)
        return self.balanced


        