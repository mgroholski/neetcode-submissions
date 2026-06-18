class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odd_cnt = (high - low) // 2

        if low % 2 or high % 2:
            odd_cnt += 1

        return odd_cnt
        