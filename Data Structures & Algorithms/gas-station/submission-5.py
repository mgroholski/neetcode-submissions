'''
We want to choose the highest 
'''


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        running = 0
        total = 0
        res = 0

        for i in range(0, len(gas)):
            total += gas[i] - cost[i]
            running += gas[i] - cost[i]
            if running < 0:
                res = i + 1
                running = 0

        return res if total >= 0 else -1

        


        
        