class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = {}

        for s in strs:
            sortedS = "".join(sorted(s))

            if sortedS not in groupings:
                groupings[sortedS] = []
            groupings[sortedS].append(s)


        res = []
        for _, v in groupings.items():
            res.append(v)
        
        return res


        