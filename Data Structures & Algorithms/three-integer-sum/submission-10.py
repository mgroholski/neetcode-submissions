class Solution:
    def twoSum(self, nums, i, sols):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum > 0:
                    k -= 1
            elif sum < 0:
                    j += 1
            else:
                    sols.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                            j += 1
        return sols


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sols = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                self.twoSum(nums, i, sols)
        return sols
    