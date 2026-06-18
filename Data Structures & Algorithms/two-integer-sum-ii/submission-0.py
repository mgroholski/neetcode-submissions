class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        totalSum = numbers[i] + numbers[j]

        while totalSum != target:
            if totalSum > target:
                j -= 1
            elif totalSum < target:
                i += 1
            totalSum = numbers[i] + numbers[j]

        return [i + 1, j + 1]