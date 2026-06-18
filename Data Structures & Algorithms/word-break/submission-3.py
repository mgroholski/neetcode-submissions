'''
This is a dynamic programming problem.

Given some substring of the input string is it a dictionary word?
We want to consider from all previous positions that made a word.


'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)

        lSet = set([0])
        for r in range(len(s) + 1):
            lSetCopy = lSet.copy()
            for l in lSetCopy:
                if s[l:r] in wordDictSet:
                    lSet.add(r)

        return len(s) in lSet
        