# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Parse and put numbers into a heap?

We should exploit the BST structure.
For any node u, all nodes to the right are greater and all nodes to the left are less than.
The problem is we don't know which way to go without knowing how many nodes there are.

How would we know if the current node is the kth smallest node?

- Create an inorder traversal
BNA

'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(u, sol):
            if u.left:
                sol = dfs(u.left, sol)

            sol.append(u.val)
        
            if u.right:
                sol = dfs(u.right, sol)

            return sol

        return dfs(root, [])[k-1]

            
        