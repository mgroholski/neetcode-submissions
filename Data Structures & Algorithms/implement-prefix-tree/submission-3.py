class PrefixTree:
    def __init__(self):
        self.isWord = False
        self.adj = {}
        
    def insert(self, word: str) -> None:
        u = self
        while len(word):
            nextLetter = word[0]
            if nextLetter not in u.adj:
                u.adj[nextLetter] = PrefixTree()
            u = u.adj[nextLetter]
            word = word[1:]
        u.isWord = True

    def search(self, word: str) -> bool:
        u = self
        while len(word):
            nextLetter = word[0]
            if nextLetter not in u.adj:
                return False
            u = u.adj[nextLetter]
            word = word[1:]
        return u.isWord

    def startsWith(self, prefix: str) -> bool:
        u = self
        while len(prefix):
            nextLetter = prefix[0]
            if nextLetter not in u.adj:
                return False
            u = u.adj[nextLetter]
            prefix = prefix[1:]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)