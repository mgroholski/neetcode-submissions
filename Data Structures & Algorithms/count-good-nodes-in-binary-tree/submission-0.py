# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, maxNum) -> int:
        if not node:
            return 0

        count = 1 if node.val >= maxNum else 0
        newMaxNum = max(maxNum, node.val)
        
        count += self.dfs(node.left, newMaxNum)
        count += self.dfs(node.right, newMaxNum)

        print(node.val, count)
        return count

    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, -101)

        
        