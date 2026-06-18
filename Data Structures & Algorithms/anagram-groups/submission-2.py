class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        f = {}

        for i in strs:
            s_i = "".join(sorted(i))
            if not s_i in f:
                f[s_i] = []

            f[s_i].append(i)
        
        return [v for v in f.values()] 

        