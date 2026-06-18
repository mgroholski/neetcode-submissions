# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxDepth = 0
        queue = [(root, 1)]
        while len(queue):
            currentNode, depth = queue.pop(0)
            maxDepth = max(maxDepth, depth)

            if currentNode.right:
                queue.append((currentNode.right, depth + 1))
            
            if currentNode.left:
                queue.append((currentNode.left, depth + 1))

        return maxDepth



        
        