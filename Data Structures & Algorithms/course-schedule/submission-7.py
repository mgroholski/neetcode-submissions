class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preDict = {i: set() for i in range(numCourses)}
        reqDict = {i: set() for i in range(numCourses)}
        takenSet = set([x for x in range(numCourses)])
        print(takenSet)

        for req, preReq in prerequisites:
            preDict[req].add(preReq)
            reqDict[preReq].add(req)
            if req in takenSet:
                takenSet.remove(req)

        stack = list(takenSet)
        while len(stack):
            currentClass = stack.pop()

            for req in reqDict[currentClass]:
                if req not in takenSet and preDict[req].issubset(takenSet):
                    stack.append(req)
                    takenSet.add(req)

        return len(takenSet) == numCourses

        

        
        