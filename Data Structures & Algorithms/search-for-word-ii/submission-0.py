class TrieNode():
    def __init__(self):
        self.charMap = {}
        self.isWord = False

    def addWord(self, word)->None:
        node = self

        while len(word):
            letter = word[0]
            if letter not in node.charMap:
                node.charMap[letter] = TrieNode()
            node = node.charMap[letter]
            word = word[1:]

        node.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        n, m = len(board[0]), len(board)
        res, visit = set(), set()

        def dfs(coordinates, node, word):            
            x,y = coordinates

            if board[x][y] not in node.charMap:
                return

            visit.add((x,y))
            node = node.charMap[board[x][y]]
            word += board[x][y]

            if node.isWord:
                res.add(word)

            for direction in [(1,0), (-1,0), (0,1), (0,-1)]:
                newX = direction[0] + x
                newY = direction[1] + y
                if 0 <= newX < m and 0 <= newY < n and (newX, newY) not in visit:
                    dfs((newX, newY), node, word)

            visit.remove((x,y))

        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs((i,j), root, "")
        return list(res)





        




        