class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda a : (a[0] ** 2)+(a[1] ** 2))
        return points[:k]
        