# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        if not root:
            return res

        queue = [(root, 0)]

        while len(queue):
            currentNode, depth = queue.pop(0)

            if depth == len(res):
                res.append([])
            
            res[depth].append(currentNode.val)

            if currentNode.left:
                queue.append((currentNode.left, depth + 1))

            if currentNode.right:
                queue.append((currentNode.right, depth + 1))

        return res
            
        