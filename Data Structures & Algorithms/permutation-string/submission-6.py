class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_f = {}
        for i in s1:
            if i not in s1_f:
                s1_f[i] = 0
            s1_f[i] += 1

        s2_f = {}
        for rIdx in range(len(s2)):
            if s2[rIdx] not in s2_f:
                s2_f[s2[rIdx]] = 0
            s2_f[s2[rIdx]] += 1

            if (rIdx + 1) - len(s1) >= 0:
                equal = True
                for i,v in s1_f.items():
                    if not i in s2_f or s2_f[i] != v:
                        equal = False
                        break

                if equal:
                    return True

                lIdx = rIdx + 1 - len(s1)
                s2_f[s2[lIdx]] -= 1
        
        return False