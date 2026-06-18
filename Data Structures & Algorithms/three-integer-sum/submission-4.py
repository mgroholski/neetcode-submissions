class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solSet = set()
        duplicateSet = set()

        for i in range(len(nums)):
            iVal = nums[i]
            if iVal not in duplicateSet:
                duplicateSet.add(iVal)
                seenSet = set()
                for j in range(i+1, len(nums)):
                    jVal = nums[j]
                    complement = - iVal - jVal
                    if complement in seenSet:
                        solSet.add(tuple(sorted((iVal, jVal, complement))))
                    seenSet.add(jVal)
        solList = []
        for i in solSet:
            solList.append(list(i))
        
        return solList
    