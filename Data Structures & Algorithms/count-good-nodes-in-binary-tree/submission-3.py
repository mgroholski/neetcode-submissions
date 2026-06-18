# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
DFS while keeping track of max val seen
'''

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        stack = [(float('-inf'), root)]
        while stack:
            maxVal, u = stack.pop()
            
            if u.val >= maxVal:
                res += 1

            maxVal = max(maxVal, u.val)
            if u.left:
                stack.append((maxVal, u.left))
            if u.right:
                stack.append((maxVal, u.right))

        return res

        