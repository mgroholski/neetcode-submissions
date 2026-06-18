'''
We can form a graph between words in wordList iff the difference is a single letter.




'''

import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if beginWord in wordSet:
            wordSet.remove(beginWord)
        if endWord not in wordSet:
            return 0
        
        queue = [(1, beginWord)]
        while queue:
            dist, u = queue.pop(0)
            if u == endWord:
                return dist

            for i in range(len(u)):
                for v in string.ascii_lowercase:
                    newWord = u[:i] + v + u[i+1:]
                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        queue.append((dist + 1, newWord))
        return 0



        