class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = Counter(s)
        remain = len(s)

        for c in t:
            if c in sCount and sCount[c] > 0:
                sCount[c] -= 1
                remain -= 1
            else:
                return False
        return remain == 0

        