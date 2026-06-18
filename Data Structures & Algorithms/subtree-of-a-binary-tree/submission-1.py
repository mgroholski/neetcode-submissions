# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def isSameTree(self, a, b):
        if not a or not b:
            return a == b

        if a.val != b.val:
            return False

        return self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return root == subRoot

        res = False
        queue = [root]
        while queue:
            u = queue.pop()

            if u.val == subRoot.val:
                res = res | self.isSameTree(u, subRoot)

            if u.left:
                queue.append(u.left)
            
            if u.right:
                queue.append(u.right)
                
        return res


       
            

        