class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        
        for i in range(len(position)):
            targetTime = (target - position[i]) / speed[i]
            
            if len(stack) == 0:
                stack.append((i, targetTime))
            else:
                tempStack = []
                if position[i] > position[stack[-1][0]]:
                    while len(stack) > 0 and position[i] > position[stack[-1][0]]:
                        idx, elementTargetTime = stack.pop()
                        if elementTargetTime > targetTime:
                            tempStack.append((idx, elementTargetTime))

                if len(stack) > 0 and position[i] < position[stack[-1][0]]:
                    if targetTime > stack[-1][1]:
                        stack.append((i, targetTime))
                else:
                    stack.append((i, targetTime))

                while len(tempStack) > 0:
                    stack.append(tempStack.pop())
                 
        return len(stack)