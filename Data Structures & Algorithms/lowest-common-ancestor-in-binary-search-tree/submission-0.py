# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getPath(self, root, p):
        path = []
        # Find path to q
        currentNode = root
        while currentNode:
            path.append(currentNode)
            if p.val == currentNode.val:
                return path
            elif p.val > currentNode.val:
                currentNode = currentNode.right
            else:
                currentNode = currentNode.left
        return path


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pPath = self.getPath(root, p)
        qPath = self.getPath(root, q)

        i = 0
        lastCommon = 0
        while i < len(pPath) and i < len(qPath):
            if pPath[i] == qPath[i]:
                print(i)
                lastCommon = pPath[i]
            i += 1

        return lastCommon

        
        