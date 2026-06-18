class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.m, self.n = len(board), len(board[0])
        self.directions = [(1,0), (-1,0), (0,-1), (0,1)]


        def search(seen, word, pos):
            word = word[1:]
            if not len(word):
                return True

            found = False
            if pos not in seen:
                seen.add(pos)
                x,y = pos

                found = False
                for dx, dy in self.directions:
                    nx, ny = dx + x, dy + y

                    if 0 <= nx < self.m and 0 <= ny < self.n and (nx, ny) not in seen and self.board[nx][ny] == word[0]:
                        found = found or search(seen, word, (nx, ny))
                    
                seen.remove(pos)
            
            return found


        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == word[0]:
                    if search(set(), word, (i,j)):
                        return True


        return False


        