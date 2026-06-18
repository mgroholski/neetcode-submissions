'''
Use all tickets at least one
'''


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = {}

        for u,v in tickets:
            if u not in adjList:
                adjList[u] = []
            adjList[u].append(v)
        
        # Ensures lexical ordering
        for i in adjList.keys():
            adjList[i].sort()

        self.res = []

        def dfs(currentLocation, path, adjList)->[str]:
            if len(path) == (len(tickets) + 1) and not len(self.res):
                self.res = path
                return 
            elif currentLocation not in adjList or not len(adjList[currentLocation]):
                return

            for i,v in enumerate(adjList[currentLocation]):
                adjList[currentLocation].pop(i)
                dfs(v, path + [v], adjList)
                adjList[currentLocation].insert(i, v)

                if len(self.res):
                    return

        dfs("JFK", ["JFK"], adjList)
        return self.res
        