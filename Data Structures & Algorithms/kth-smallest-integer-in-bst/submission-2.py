# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.kSmallestVal = 0

        def dfs(node, count) -> int:
            if not node:
                return 0

            if node.left:
                count += dfs(node.left, count) - count

            count += 1

            print(node.val, count)
            if count == k:
                self.kSmallestVal = node.val

            if node.right:
                count += dfs(node.right, count) - count
            
            return count
        
        dfs(root, 0)
        return self.kSmallestVal