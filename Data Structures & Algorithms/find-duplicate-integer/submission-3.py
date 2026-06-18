'''
Fast and slow pointer

slowPtr moves once when fastPtr moves twice



'''


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slowPtr = nums[0]
        fastPtr = nums[0]

        start = False
        while not start or (slowPtr != fastPtr):
            start = True
            slowPtr = nums[slowPtr]
            fastPtr = nums[nums[fastPtr]]

        startPtr = nums[0]
        while slowPtr != startPtr:
            slowPtr = nums[slowPtr]
            startPtr = nums[startPtr]

        return startPtr


        