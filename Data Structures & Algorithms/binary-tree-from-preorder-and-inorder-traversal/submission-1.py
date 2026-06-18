# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Preorder: NLR
Inorder: LNR

preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]

Node = 3 
Left most node = 9

We can make recursive calls to make subtrees

'''



class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        rootVal = preorder[0]
        root = TreeNode(val=rootVal)
        mid = inorder.index(rootVal)

        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root

        