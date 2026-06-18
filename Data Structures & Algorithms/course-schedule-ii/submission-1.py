class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preList = {i : set() for i in range(numCourses)}
        reqList = {i : set() for i in range(numCourses)}
        takenSet = set([i for i in range(numCourses)])

        for req, preReq in prerequisites:
            preList[req].add(preReq)
            reqList[preReq].add(req)

            if req in takenSet:
                takenSet.remove(req)

        takenList = []
        queue = list(takenSet)

        while len(queue):
            currentClass = queue.pop(0)
            takenList.append(currentClass)

            for req in reqList[currentClass]:
                if req not in takenSet and preList[req].issubset(takenSet):
                    queue.append(req)
                    takenSet.add(req)

        return [] if len(takenSet) != numCourses else takenList
        