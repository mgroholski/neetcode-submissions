class PrefixNode:
    def __init__(self):
        self.charMap = {}
        self.isWord = False


class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()
        
    def insert(self, word: str) -> None:
        currentNode = self.root

        while len(word):
            currentLetter = word[0]
            if currentLetter not in currentNode.charMap:
                currentNode.charMap[currentLetter] = PrefixNode()
            currentNode = currentNode.charMap[currentLetter]
            word = word[1:]

        currentNode.isWord = True

    def search(self, word: str) -> bool:
        currentNode = self.root

        while len(word):
            currentLetter = word[0]
            if currentLetter not in currentNode.charMap:
                return False
            currentNode = currentNode.charMap[currentLetter]
            word = word[1:]
        
        return currentNode.isWord
        

    def startsWith(self, prefix: str) -> bool:
        currentNode = self.root

        while len(prefix):
            currentLetter = prefix[0]
            if currentLetter not in currentNode.charMap:
                return False
            currentNode = currentNode.charMap[currentLetter]
            prefix = prefix[1:]
        return True
        
        