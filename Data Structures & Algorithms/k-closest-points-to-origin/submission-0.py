import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            distance = ((point[0] - 0) ** 2 + (point[1] - 0) ** 2) ** (0.5)
            heapq.heappush(heap, (distance, point))

        return [x[1] for x in heapq.nsmallest(k, heap)]