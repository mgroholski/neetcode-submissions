# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        stack = [root]
        while len(stack):
            currentNode = stack.pop()
            
            currentNodeRight = currentNode.right
            currentNodeLeft = currentNode.left

            currentNode.left = currentNodeRight
            currentNode.right = currentNodeLeft

            if currentNodeRight:
                stack.append(currentNodeRight)

            if currentNodeLeft:
                stack.append(currentNodeLeft)
                
        return root
