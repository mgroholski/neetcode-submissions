"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        nodeToVal = {}
        def dfs(u):
            nonlocal nodeToVal
            if u.val in nodeToVal:
                return nodeToVal[u.val]
            
            nodeToVal[u.val] = Node(u.val, [])
            for v in u.neighbors:
                nodeToVal[u.val].neighbors.append(dfs(v))

            return nodeToVal[u.val]

        return dfs(node)