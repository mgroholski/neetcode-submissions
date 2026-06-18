'''
nums = [2,3,1,1,4]

x = 4 -> 4 + 4
x = 4 -> 3 + 1 >= 4
x = 3 -> 2 + 1 >= 3
x = 2 -> 1 + 3 >= 2
x = 1 -> 



'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        x = len(nums) - 1

        for i in range(len(nums) - 1, -1 , -1):
            if nums[i] + i >= x:
                x = i

        return x == 0

        
        