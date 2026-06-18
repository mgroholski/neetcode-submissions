class Node:
    def __init__(self, val):
        self.val = val
        self.preReqs = set()
        self.reqs = set()

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites and numCourses:
            return True

        # Create graph
        takenClasses = set()
        classes = {}
        for i in range(numCourses):
            classes[i] = Node(i)
            takenClasses.add(i)

        for relation in prerequisites:            
            if relation[1] not in classes:
                classes[relation[1]] = Node(relation[1])
            preReq = classes[relation[1]]

            if relation[0] not in classes:
                classes[relation[0]] = Node(relation[0])
            req = classes[relation[0]]

            req.preReqs.add(preReq)
            preReq.reqs.add(req)

            if req.val in takenClasses:
                takenClasses.remove(req.val)

        stack = [x for x in takenClasses]
        while len(stack):
            print(takenClasses)
            currentClass = classes[stack.pop()]

            for nextClass in currentClass.reqs:
                if set([x.val for x in nextClass.preReqs]).issubset(takenClasses):
                    stack.append(nextClass.val)
                    takenClasses.add(nextClass.val)

        return len(takenClasses) == numCourses