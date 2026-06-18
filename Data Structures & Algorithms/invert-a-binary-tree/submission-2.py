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

        queue = [root]
        while queue:
            for _ in range(len(queue)):
                n = queue.pop(0)
                n.right, n.left = n.left, n.right

                if n.right:
                    queue.append(n.right)

                if n.left:
                    queue.append(n.left)

        return root
