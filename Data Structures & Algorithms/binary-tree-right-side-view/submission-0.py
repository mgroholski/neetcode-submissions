# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        if not root:
            return res

        stack = [(root, 0)]
        shieldedDepth = -1
        while len(stack):
            currentNode, depth = stack.pop()

            if depth > shieldedDepth:
                res.append(currentNode.val)
                shieldedDepth = depth

            if currentNode.left:
                stack.append((currentNode.left, depth + 1))
            
            if currentNode.right:
                stack.append((currentNode.right, depth + 1))

        return res