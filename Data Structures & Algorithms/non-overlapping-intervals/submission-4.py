class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda a : a[1])

        ans = 0
        k = float('-inf')

        for u,v in intervals:
            if u >= k:
                k = v
            else:
                ans += 1

        return ans