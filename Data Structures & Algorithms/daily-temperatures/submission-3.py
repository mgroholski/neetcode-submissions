'''
For each index we want to know, when the next time it's warmer

This seems like a stack problem 


temperatures = [73,74,75,71,69,72,76,73]

res = [1,1,0,0,0,0,0,0]
stack = [(75,2), (71,3), (69,4), ()]


'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while len(stack) and stack[-1][0] < temp:
                _, i = stack.pop()
                res[i] = idx - i
            stack.append((temp, idx))

        return res

        