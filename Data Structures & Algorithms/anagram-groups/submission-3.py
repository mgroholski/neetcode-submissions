class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            sortedWord = "".join(sorted(list(s)))
            if sortedWord not in groups:
                groups[sortedWord] = []
            groups[sortedWord].append(s)

        return [a for a in groups.values()]



        