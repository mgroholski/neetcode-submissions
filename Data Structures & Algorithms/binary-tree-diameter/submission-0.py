# max(two branches or up)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:    
        self.res = 0

        def dfs(root) -> int:
            if not root:
                return 0

            leftVal = dfs(root.left)
            rightVal = dfs(root.right)

            self.res = max(self.res, leftVal + rightVal)
            return max(leftVal, rightVal) + 1
        
        dfs(root)
        return self.res
    





        