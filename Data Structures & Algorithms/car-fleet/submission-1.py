'''
Stack problem

If a car catches up to another car in front of it, they combine. We want to find how many groupings.

When does a car catch up?
 - If two adjacent cars meet before the end. We can caclulate when they meet by
    s_1x-s_2x = y_2-y_1
    (y_2 - y_1)/(s_1 - s_ 2) = x

s_1x + p_1 = s_2x + p_2


Sort by position. For each adjacent position, determine if combine or not

'''
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        cars = sorted(zip(position, speed), reverse=True)
        for p,s in cars:
            arrive_time = (target - p)/s
            if not stack or stack[-1] < arrive_time:
                stack.append(arrive_time)

        return len(stack)

        


        