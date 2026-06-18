'''
return the number fo words in the shortest transformation sequence from beginWord to endWord
or 0 if none exists

each adjacent word in the ladder differs by a single letter

each word is in word list (begin word does not need to be)
'''
class TrieNode:
    def __init__(self):
        self.charMap = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root

        for c in word:
            if c not in node.charMap:
                node.charMap[c] = TrieNode()
            node = node.charMap[c]

        node.isWord = True

    def findWords(self, word)->List[str]:
        res = []

        stack = [(self.root, "", word)]
        while len(stack):
            node, prefix, w = stack.pop()

            if not len(w) and node.isWord:
                res.append(prefix)
                continue
            elif not len(w):
                continue

            nextLetter = w[0]

            if nextLetter == "*":
                for key, val in node.charMap.items():
                    stack.append((val, prefix + key, w[1:]))
            elif nextLetter in node.charMap:
                stack.append((node.charMap[nextLetter], prefix + nextLetter, w[1:]))

        return res


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        if beginWord not in wordList:
            wordList.append(beginWord)
        
        trie = Trie()
        for i in wordList:
            trie.addWord(i)
        
        adjList = {}
        for i in wordList:
            adjList[i] = set()

            for j in range(len(i)):
                wildcard = i[:j] + "*"
                if j + 1 < len(i):
                    wildcard += i[j + 1:]
                adjList[i] = adjList[i].union(set(trie.findWords(wildcard)))
            adjList[i].remove(i)

        # Dijkstras Algorithm
        minHeap = [(0, beginWord, None)]
        distances = {word : float('inf') for word in wordList}

        while len(minHeap):
            distance, word, previousWord = heapq.heappop(minHeap)

            if distances[word] != float('inf'):
                continue

            if not previousWord:
                distances[word] = 1
            else:
                distances[word] = distance + 1

            for neighbor in adjList[word]:
                heapq.heappush(minHeap, (distance + 1, neighbor, word))
        
        return distances[endWord] if distances[endWord] != float('inf') else 0




        



        