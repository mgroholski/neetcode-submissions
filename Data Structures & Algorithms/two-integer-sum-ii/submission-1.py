class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers) - 1

        cur_sum = numbers[l] + numbers[r]
        while cur_sum != target:
            if cur_sum > target:
                r -= 1
            else:
                l += 1

            cur_sum = numbers[l] + numbers[r]
        
        return [l + 1, r + 1]