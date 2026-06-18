'''
Given a list of words from the alien languages dictionary, return whether it's possible the words are sorted lexicographically.

If multiple solutions exist, return any. If none, return "".

'''

from collections import OrderedDict

class TrieNode:
    def __init__(self):
        self.charDict = OrderedDict()

    def addWord(self, word)->bool:
        node = self

        while len(word):
            letter = word[0]
            if letter not in node.charDict:
                node.charDict[letter] = TrieNode()
            elif next(reversed(node.charDict)) != letter:
                return False
            node = node.charDict[letter] 
            word = word[1:]

        if len(node.charDict) != 0:
            return False

        return True


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        root = TrieNode()

        for word in words:
            if not root.addWord(word):
                return ""

        # Build adjList
        adjDict = {}

        queue = [root]
        while len(queue):
            node = queue.pop(0)

            keysList = list(node.charDict.keys())
            for i,c in enumerate(keysList):
                if c not in adjDict:
                    adjDict[c] = []
                if i + 1 < len(keysList):
                    adjDict[c] += keysList[i + 1:]
                queue.append(node.charDict[c])

        revAdjDict = {}
        for i,l in adjDict.items():
            if i not in revAdjDict:
                revAdjDict[i] = []
            for v in l:
                if v not in revAdjDict:
                    revAdjDict[v] = []
                revAdjDict[v].append(i)

        # Topological sort
        res = ""
        startList = []
        for i,v in revAdjDict.items():
            if not len(v):
                startList.append(i)

        while len(startList):
            u = startList.pop(0)

            res += u
            for v in adjDict[u]:
                revAdjDict[v].remove(u)
                if not len(revAdjDict[v]):
                    startList.append(v)

        if len(res) != len(adjDict.keys()):
            return ""

        return res



