# for n in nodes
# if n hasn't been seen
#  componentCount += 1
#  bfs from n marking all nodes as seen

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i: set() for i in range(n)}

        for u,v in edges:
            adjList[u].add(v)
            adjList[v].add(u)

        seenSet = set()
        componentCount = 0

        for u in range(n):
            if u not in seenSet:
                componentCount += 1
                queue = [u]
                seenSet.add(u)
                while len(queue):
                    node = queue.pop(0)

                    for v in adjList[node]:
                        if v not in seenSet:
                            seenSet.add(v)
                            queue.append(v)
        return componentCount



        