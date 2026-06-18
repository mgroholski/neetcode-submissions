class TrieNode:
    def __init__(self):
        self.charMap = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word: str) -> None:
        currentNode = self.root
        
        for c in word:
            if c not in currentNode.charMap:
                currentNode.charMap[c] = TrieNode()
            
            currentNode = currentNode.charMap[c]

        currentNode.isWord = True
        

    def searchWord(self, word: str) -> bool:
        def backtrack(currentNode, word) -> bool:
            if not len(word):
                return currentNode.isWord

            currentLetter = word[0]

            if currentLetter == ".":
                foundWord = False
                for node in currentNode.charMap.values():
                    if backtrack(node, word[1:]):
                        foundWord = True
                        break
                return foundWord
            elif currentLetter in currentNode.charMap:
                return backtrack(currentNode.charMap[currentLetter], word[1:])
            return False
        return backtrack(self.root, word)

class WordDictionary:

    def __init__(self):
        self.trie = Trie()
        
    def addWord(self, word: str) -> None:
        self.trie.add(word)
        
    def search(self, word: str) -> bool:
        return self.trie.searchWord(word)
        
