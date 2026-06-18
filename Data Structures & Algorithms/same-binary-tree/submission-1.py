# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return p == q
        
        pQueue = [p]
        qQueue = [q]

        while pQueue and qQueue:
            p = pQueue.pop(0)
            q = qQueue.pop(0)

            if p.val != q.val:
                return False

            pRight = not p.right is None
            pLeft = not p.left is None

            qRight = not q.right is None
            qLeft = not q.left is None

            if pRight != qRight or pLeft != qLeft:
                return False

            if p.left:
                pQueue.append(p.left)
            if p.right:
                pQueue.append(p.right)

            if q.left:
                qQueue.append(q.left)
            if q.right:
                qQueue.append(q.right)


        return True

