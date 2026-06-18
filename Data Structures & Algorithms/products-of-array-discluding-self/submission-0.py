class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        
        leftList = []
        leftList.append(nums[0])
        for i in range(1, len(nums)):
            leftList.append(leftList[i - 1] * nums[i])
        
        rightList = [0] * len(nums) 
        rightList[-1] = (nums[-1])
        for i in range(len(nums) - 2, -1, -1):
            rightList[i] = (rightList[i + 1] * nums[i])
        
        for i in range(len(nums)):
            leftValue = 1 if i == 0 else leftList[i - 1]
            rightValue = 1 if i == len(nums) - 1 else rightList[i + 1]
            output.append(leftValue * rightValue)
        
        return output