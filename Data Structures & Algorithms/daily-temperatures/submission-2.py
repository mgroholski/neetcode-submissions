'''
temperatures = [30,38,30,36,35,40,28]

res = [0,0,1,2,1,0,0]
stack = [(40,5), ]
'''


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        
        stack = []
        for idx in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[idx]

            while stack and stack[-1][0] <= temp:
                stack.pop()

            if stack:
                res[idx] = stack[-1][1] - idx

            stack.append((temp, idx))

        return res


        