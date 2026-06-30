class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        seen = []

        res = [0 for _ in range(len(temperatures))]

        for idx, temp in enumerate(temperatures):
            while len(seen) and seen[-1][0] < temp:
                _, last_idx = seen.pop()

                res[last_idx] = idx - last_idx

            seen.append((temp, idx))

        return res
        