# Can there be duplicate values? No

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        cloneDict = {}

        queue = [node]
        seenSet = set([node])

        while len(queue):
            currentNode = queue.pop(0)
            if currentNode.val not in cloneDict:
                cloneDict[currentNode.val] = Node(currentNode.val)
            newNode = cloneDict[currentNode.val]

            for neighbor in currentNode.neighbors:
                if neighbor.val not in cloneDict:
                    cloneDict[neighbor.val] = Node(neighbor.val)
                neighborNode = cloneDict[neighbor.val]
                newNode.neighbors.append(neighborNode)

                if neighbor not in seenSet:
                    queue.append(neighbor)
                    seenSet.add(neighbor)
            
        return cloneDict[node.val]
            



        
        