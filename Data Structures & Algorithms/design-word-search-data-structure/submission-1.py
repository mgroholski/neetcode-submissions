'''
Trie data structure

We'll create a tree where each node is a letter
At each node, we'll want an adjDict to next letters and if it is a word


'''


class WordDictionary:
    def __init__(self):
        self.isWord = False
        self.adjDict = {}

    def addWord(self, word: str) -> None:
        u = self
        queue = list(word)
        while queue:
            nextLetter = queue.pop(0)

            if not nextLetter in u.adjDict:
                u.adjDict[nextLetter] = WordDictionary()
            u = u.adjDict[nextLetter]
        u.isWord = True        
        
    def search(self, word: str) -> bool:
        if not len(word):
            return self.isWord

        nextLetter = word[0]
        res = False
        if nextLetter == '.':
            for v in self.adjDict.values():
                res = res or v.search(word[1:])
        else:
            if nextLetter in self.adjDict:
                res = self.adjDict[nextLetter].search(word[1:])
        return res


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)