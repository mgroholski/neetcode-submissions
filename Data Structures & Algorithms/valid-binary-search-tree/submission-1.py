# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryDFS(self, node, minVal, maxVal) -> bool:
        if not node:
            return True

        currentValue = node.val
        if minVal < currentValue < maxVal:
            isLeftValid = self.binaryDFS(node.left, minVal, min(currentValue, maxVal))
            isRightValid = self.binaryDFS(node.right, max(currentValue, minVal), maxVal)

            return isLeftValid and isRightValid
        else:
            return False

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.binaryDFS(root, float('-inf'), float('inf'))